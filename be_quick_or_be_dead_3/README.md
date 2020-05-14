# Be Quick Or Be Dead 3
As the [song](https://www.youtube.com/watch?v=CTt1vk9nM9c) draws closer to the end, another executable [be-quick-or-be-dead-3](be-quick-or-be-dead-3) suddenly pops up. This one requires even faster machines. Can you run it fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-3_4_081de19947195d5a491290bc42530db6.

## Solution
The solution to this problem is very similar to the other `be_quick_or_be_dead_*` in the series. This time the key was some weird function. Using [radare2](https://en.wikipedia.org/wiki/Radare2) I reverse engineered the binary and converted the assembly code to pseudocode.

```
 $ r2 be-quick-or-be-dead-3
[0x004005a0]> aaa
[0x004005a0]> s sym.calc
[0x00400706]> pdf
            ; XREFS: CALL 0x00400733  CALL 0x00400742  CALL 0x00400751  CALL 0x00400761  CALL 0x00400776  CALL 0x0040079b  
┌ 140: sym.calc (signed int arg1);
│           ; var signed int var_24h @ rbp-0x24
│           ; var int64_t var_14h @ rbp-0x14
│           ; arg signed int arg1 @ rdi
│           0x00400706      55             push rbp
│           0x00400707      4889e5         mov rbp, rsp
│           0x0040070a      4154           push r12
│           0x0040070c      53             push rbx
│           0x0040070d      4883ec20       sub rsp, 0x20
│           0x00400711      897ddc         mov dword [var_24h], edi    ; arg1
│           0x00400714      837ddc04       cmp dword [var_24h], 4
│       ┌─< 0x00400718      7711           ja 0x40072b
│       │   0x0040071a      8b45dc         mov eax, dword [var_24h]
│       │   0x0040071d      0faf45dc       imul eax, dword [var_24h]
│       │   0x00400721      0545230000     add eax, 0x2345
│       │   0x00400726      8945ec         mov dword [var_14h], eax
│      ┌──< 0x00400729      eb5b           jmp 0x400786
│      ││   ; CODE XREF from sym.calc @ 0x400718
│      │└─> 0x0040072b      8b45dc         mov eax, dword [var_24h]
│      │    0x0040072e      83e801         sub eax, 1
│      │    0x00400731      89c7           mov edi, eax
│      │    0x00400733      e8ceffffff     call sym.calc
│      │    0x00400738      89c3           mov ebx, eax
│      │    0x0040073a      8b45dc         mov eax, dword [var_24h]
│      │    0x0040073d      83e802         sub eax, 2
│      │    0x00400740      89c7           mov edi, eax
│      │    0x00400742      e8bfffffff     call sym.calc
│      │    0x00400747      29c3           sub ebx, eax
│      │    0x00400749      8b45dc         mov eax, dword [var_24h]
│      │    0x0040074c      83e803         sub eax, 3
│      │    0x0040074f      89c7           mov edi, eax
│      │    0x00400751      e8b0ffffff     call sym.calc
│      │    0x00400756      4189c4         mov r12d, eax
│      │    0x00400759      8b45dc         mov eax, dword [var_24h]
│      │    0x0040075c      83e804         sub eax, 4
│      │    0x0040075f      89c7           mov edi, eax
│      │    0x00400761      e8a0ffffff     call sym.calc
│      │    0x00400766      4129c4         sub r12d, eax
│      │    0x00400769      4489e0         mov eax, r12d
│      │    0x0040076c      01c3           add ebx, eax
│      │    0x0040076e      8b45dc         mov eax, dword [var_24h]
│      │    0x00400771      83e805         sub eax, 5
│      │    0x00400774      89c7           mov edi, eax
│      │    0x00400776      e88bffffff     call sym.calc
│      │    0x0040077b      69c034120000   imul eax, eax, 0x1234
│      │    0x00400781      01d8           add eax, ebx
│      │    0x00400783      8945ec         mov dword [var_14h], eax
│      │    ; CODE XREF from sym.calc @ 0x400729
│      └──> 0x00400786      8b45ec         mov eax, dword [var_14h]
│           0x00400789      4883c420       add rsp, 0x20
│           0x0040078d      5b             pop rbx
│           0x0040078e      415c           pop r12
│           0x00400790      5d             pop rbp
└           0x00400791      c3             ret
[0x00400706]> 
```

### Pseudocode
Below is the translation of the assembly code above. **Notice** how there is repeated calculations of sub-problems. This function is a good candidate for (dynamic programming)[https://en.wikipedia.org/wiki/Dynamic_programming].

```
def calc(x):
 if x > 4:
	 x1 = calc(x - 1)
	 x2 = calc(x - 2)
	 
	 y1 = x1 - x2

	 x3 = calc(x - 3)
	 x4 = calc(x - 4)

	 y2 = x3 - x4

	 y3 = y1 + y2

	 x5 = calc(x - 5) * 0x1234

	 return y3 + x5
 else:
	 return (x * x) + 0x2345
```


### Optimized C Code

```
/**
 * calc_key.c
 */
int calc(int x) {
  if (x <= 4) {
    return (x * x) + 0x2345;
  }
  
  int x0 = (0 * 0) + 0x2345;
  int x1 = (1 * 1) + 0x2345;
  int x2 = (2 * 2) + 0x2345;
  int x3 = (3 * 3) + 0x2345;
  int x4 = (4 * 4) + 0x2345;
  
  for (int i = 5; i <= x; i++) {
    int y1 = x4 - x3;
    int y2 = x2 - x1;
    int y3 = y1 + y2;
    int y4 = x0 * 0x1234;
    int next = y3 + y4;

    // shift all for next iteration
    x0 = x1;
    x1 = x2;
    x2 = x3;
    x3 = x4;
    x4 = next;
  }

  return x4;
}
```

## Exploit
The exploit is to patch the binary in such a way that it does not execute the `sym.calc` function. Rather it returns the final value. Using Radare2 we get:

```
# Get the key
$ ./calc_key                                                                                       
2f8cdc3f

# Start radare2 in debug mode and navigate to the sym.calculate_key function.
# Note: I know that the key function is being called in `calculate_key()` because
# the layout of this binary is similar to previous problems in this serie.

$ r2 -d be-quick-or-be-dead-3                                                                      
[0x7e84ece0bc20]> aaa
[0x7e84ece0bc20]> s sym.calculate_key
[0x00400792]> pdf
            ; CALL XREF from sym.get_key @ 0x400828
┌ 16: sym.calculate_key ();
│           0x00400792      55             push rbp
│           0x00400793      4889e5         mov rbp, rsp
│           0x00400796      bf4b8f0100     mov edi, 0x18f4b
│           0x0040079b      e866ffffff     call sym.calc
│           0x004007a0      5d             pop rbp
└           0x004007a1      c3             ret
```

Now we set the position of radare2 at `0x0040079b`, the address where the `calc()` function is being called. Then we ask radare2 what the bytes should be for the operation `mov eax, 0x2f8cdc3f`. We get `wx b83fdc8c2f`. Thus we enter `wx b83fdc8c2f` to override the call to `calc()` and tell radare2 to execute the binary using `dc`.

```
[0x00400792]> s 0x0040079b
[0x0040079b]> wa* mov eax, 0x2f8cdc3f
wx b83fdc8c2f
[0x0040079b]> wx b83fdc8c2f
[0x0040079b]> dc
Be Quick Or Be Dead 3
=====================

Calculating key...
Done calculating key
Printing flag:
picoCTF{dynamic_pr0gramming_ftw_22ac7d81}
[0x7e84ecb24618]> Q
```

The flag is `picoCTF{dynamic_pr0gramming_ftw_22ac7d81}`.


## Hints
- How do you speed up a very repetitive computation?
