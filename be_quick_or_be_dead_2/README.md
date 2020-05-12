# Be Quick Or Be Dead 2
As you enjoy this [music](https://www.youtube.com/watch?v=CTt1vk9nM9c) even more, another executable [be-quick-or-be-dead-2](be-quick-or-be-dead-2) shows up. Can you run this fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-2_0_04f4c579185361da6918bbc2fc9dcb7b.


## Solution
The solution to this problem involved patching the binary with the final value of the `key`. This binary calculates a `key` that is used to decrypt the flag. Using [Radare2](https://en.wikipedia.org/wiki/Radare2) I discovered that the key is a [fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number).

```
$ r2 -d be-quick-or-be-dead-2
[0x7dfd48e03c20]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7dfd48e03c20]> s sym.calculate_key
[0x0040074b]> pdf
            ; CALL XREF from sym.get_key @ 0x4007e1
┌ 16: sym.calculate_key ();
│           0x0040074b      55             push rbp
│           0x0040074c      4889e5         mov rbp, rsp
│           0x0040074f      bff7030000     mov edi, 0x3f7              ; 1015
│           0x00400754      e8adffffff     call sym.fib
│           0x00400759      5d             pop rbp
└           0x0040075a      c3             ret
[0x0040074b]> 
```

Thus the key is `F_1015`. This number will surely [overflow](https://en.wikipedia.org/wiki/Integer_overflow). Thus, I wrote a simple program to output the bytes that that would be returned by `fib(1015)`.

### get_key.c
```
#include <stdint.h>
#include <stdio.h>

const int SEED = 1015;

int fib(const int n) {
  int prev = 0;
  int next = 1;

  for (int i = 2; i <= n; i++) {
    int tmp = prev + next;
    prev = next;
    next = tmp;
  }

  return next;
}

int main() {
  printf("%x\n", fib(SEED));
  return 0;
}
```

```
$ ./get_key 
d73ec32d
```

To get the flag we need to patch this file so that instead of calling `sym.fib` at address `0x00400754` we are setting `eax` (the return value) to be `0xd73ec32d`.


## Exploit
We use `wa*` to figure out the exact bytes to write at location `0x00400754`. So `wa* mov eax, 0xd73ec32d` returns `wx b82dc33ed7`. Thus if we set radare to go to the instruction, `s 0x00400754`, and exeucte `wx b82dc33ed7`, then the `call sym.fib` instruction would be overwritten.

Lastly, when we run the application using `dc` the flag would be printed `picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}`.

```
$ radare2 -d be-quick-or-be-dead-2
Process with PID 4285 started...
= attach 4285 4285
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
Warning: r_bin_file_hash: file exceeds bin.hashlimit
 -- See you in shell
[0x7a317f792c20]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x7a317f792c20]> s sym.calculate_key
[0x0040074b]> pdf
            ; CALL XREF from sym.get_key @ 0x4007e1
┌ 16: sym.calculate_key ();
│           0x0040074b      55             push rbp
│           0x0040074c      4889e5         mov rbp, rsp
│           0x0040074f      bff7030000     mov edi, 0x3f7              ; 1015
│           0x00400754      e8adffffff     call sym.fib
│           0x00400759      5d             pop rbp
└           0x0040075a      c3             ret
[0x0040074b]> s 0x00400754
[0x00400754]> wa* mov eax, 0xd73ec32d
wx b82dc33ed7
[0x00400754]> wx b82dc33ed7
[0x00400754]> dc
Be Quick Or Be Dead 2
=====================

Calculating key...
Done calculating key
Printing flag:
picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}
[0x7a317f4ab618]> Q
```


## Hints
- Can you call stuff without executing the entire program?
- What will the key finally be?
