# PIE TIME

Can you try to get the flag? Beware we have PIE!

* The source code could be found [here](./vuln.c).
* The binary could be found [here](./vuln).

# Solution

Looking at the source code [vuln.c](./vuln.c), we see that that the `win()` function is where the flag is read and printed.

Thus, to solve this problem, we'll use two terminals and `gdb`.

In terminal 01, execute the binary:

```shell
./vuln
```

```shell
Address of main: 0x5d9a19d6f33d
Enter the address to jump to, ex => 0x12345:
```

In terminal 02, we use `gdb` to find the offset of the `win()` function and `main()` then subtract this offset from the address of main `0x5d9a19d6f33d`.

```shell
gdb --quiet -ex "print/x 0x62ce98cd633d - (main-win)" -ex "quit" ./vuln
```
```shell
$1 = 0x62ce98cd62a7
```

We subtract the offset amount `(main - win)` from the address because the stack grows downwards in `x86` and `x86-64` architectures.

Using the address `0x62ce98cd62a7` that we get from `gdb` we could provide it as input to the program running in terminal 01 and get the flag.

```shell
Address of main: 0x62ce98cd633d
Enter the address to jump to, ex => 0x12345: 0x62ce98cd62a7
Your input: 62ce98cd62a7
You won!
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_31cc212b}
```

# Flag

```shell
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_31cc212b}
```

# Hints

1. Can you figure out what changed between the address you found locally and in the server output?