# Wave a Flag
Can you invoke help flags for a tool or binary? [This program](warm) has extraordinarily helpful information...


## Hints
1. This program will only work in the webshell or another Linux computer.
1. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`
1. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
1. `-h` and `--help` are the most common arguments to give to programs to get more information from them!
1. Not every program implements help features like `-h` and `--help`.


### Solution
The flag is in the help section of the program. By executing the binary with the `-h` argument we could get the flag.

```
chmod 500 warm
./warm -h | grep -o 'picoCTF{.*}'
```


#### Flag
```
picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
