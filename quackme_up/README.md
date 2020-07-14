# Quackme Up
The duck puns continue. Can you crack, I mean quack this [program](main) as well? You can find the program in `/problems/quackme-up_0_740a9bce2dc2d486c687b9d3a6835d73` on the shell server.


## Solution

Notice that sending the program the same character as input returns the same ciphertext in the output:

```
$ ./main 
We're moving along swimmingly. Is this one too fowl for you?
Enter text to encrypt: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Here's your ciphertext: 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02
Now quack it! : 11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1
That's all folks.
```

That is, the character `A` is always encrypted to ciphertext `02`.


Thus to crack the flag, we send the program a list of printable ascii characters:

```
$ cat printable_ascii.txt 
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

$ ./main < printable_ascii.txt 
We're moving along swimmingly. Is this one too fowl for you?
Enter text to encrypt: Here's your ciphertext: 04 34 24 54 44 74 64 94 84 B4 A4 D4 C4 F4 E4 15 05 35 25 55 45 75 65 95 85 B5 A5 D5 C5 F5 E5 12 02 32 22 52 42 72 62 92 82 B2 A2 D2 C2 F2 E2 13 03 33 23 53 43 73 63 93 83 B3 A3 D3 C3 F3 E3 10 00 30 20 50 40 70 60 90 80 B0 A0 D0 C0 F0 E0 11 01 31 21 51 41 71 61 91 81 B1 A1 D1 C1 F1
Now quack it! : 11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1
That's all folks.
```

Using the encrypted text and the printable ascii characters,we could construct a map:
```
ciphertext_character -> ascii_character
```

### Exploit
I took the output from the program above, added it to files [printable_ascii_ciphertext.txt](printable_ascii_ciphertext.txt) and [flag_ciphertext.txt](flag_ciphertext.txt) and then wrote a Python program [crack.py](crack.py) to create the `ciphertext_character -> ascii_character` map and use that map to crack the flag ciphertext.

```
$ python crack.py 
picoCTF{qu4ckm3_cba512e7}
```

Thus the flag is `picoCTF{qu4ckm3_cba512e7}`.
