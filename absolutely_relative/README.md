# Absolutely Relative

In a filesystem, everything is relative ¯\_(ツ)_/¯. Can you find a way to get a flag from this program? You can find it in /problems/absolutely-relative_4_bef88c36784b44d2585bb4d2dbe074bd on the shell server. Source.

## Solution
SSH onto the server and create a symbolic link, of the executable, in your home directory.

```
$ cd ~
$ ln -s /problems/absolutely-relative_4_bef88c36784b44d2585bb4d2dbe074bd/absolutely-relative absolutely-relative
```

Create a `permission.txt` file in your home directory that the program could read.

```
$ echo "yes" > permission.txt 
$ cat permission.txt 
yes
```

Execute the program and the flag will be printed.

```
$ cd ~
$ ./absolutely-relative 
You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_3b69633f}
```
