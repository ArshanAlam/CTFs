# Assembly 2
What does `asm2(0xe,0x21)` return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](loop_asm_rev.S) located in the directory at /problems/assembly-2_3_c3ee3603bd2a8e682f1d64cf6dfd21fb.


## Solution
Here is my analysis:


```
.intel_syntax noprefix
.bits 32

.global asm2

# asm2(0xe,0x21)
# ebp+0x8 <- 0xe
# ebp+0xc <- 0x21
asm2:
  push          ebp
  mov           ebp,esp
  sub           esp,0x10
  # eax <- 0x21
  mov           eax,DWORD PTR [ebp+0xc]
  # ebp-0x4 <- 0x21
  mov   DWORD PTR [ebp-0x4],eax
  # eax <- 0xe
  mov           eax,DWORD PTR [ebp+0x8]
  # ebp-0x8 <- 0xe
  mov   DWORD PTR [ebp-0x8],eax
  jmp           part_b
part_a:
  # add 0x1 to 0x21 at each iteration
  add           DWORD PTR [ebp-0x4],0x1
  # add 0x41 to whatever is in ebp+0x8
  add   DWORD PTR [ebp+0x8],0x41
part_b:
  # iteration 0: compare 0xe to 0x9886
  #           1: 0xe + 0x41 to 0x9886
  #           2: 0xe + 0x41 + 0x41 to 0x9886
  #           ...
  # So the number of iterations is (0x9886 - 0xe)/(0x41) = d(39046 - 14)/d(65) ~ d(601) = 0x259
  cmp           DWORD PTR [ebp+0x8],0x9886
  jle           part_a
  # ebp-0x4 <- 0x27A = 0x21 + 0x259
  mov           eax,DWORD PTR [ebp-0x4]
  mov   esp,ebp
  pop   ebp
  ret
```


## Hints
- assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
