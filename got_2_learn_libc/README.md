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


#### Why use `mkfifo`
Since the `./vuln` binary is using [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization), and we need to compute the address for the libc `system` function, we need a way to send bytes to the `stdin` of `./vuln` from `./generate_shellcode.py`.

We do this by using [named pipes](https://en.wikipedia.org/wiki/Named_pipe).

We `cat` the data from a named pipe called `named_pipe`  into `./vuln`. That way the input for `./vuln` is whatever that is written to `named_pipe`. To write bytes to `named_pipe`, we write to the file in `./generate_shellcode.py`.


## Exploit
To execute this exploit we will need three terminal windows:

1. terminal window 1 will execute `./exploit_run_vuln.sh`. This will create the named pipe called `named_pipe`.
2. terminal window 2 will run `cat > named_pipe`. This will keep the stdin open for `./vuln` (which is being execute in `exploit_run_vuln.sh`) *note: This terminal will be used to send commands to the shell once we get ourself a shell*
3. terminal window 3 will execute `./generate_shellcode.py` to generate the shellcode and write it to `named_pipe`



