# Blaise's Cipher 

My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with `nc 2018shell.picoctf.com 26039`.


## Solution
The solution to this problem involved implementing a decoder for [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). I managed to crack the key using brute force because the `key size = 4` was small. However after cracking the key and getting the flag I also wrote a function to extact the cyclical key given the ciphertext (`pohzCZK`) and the known plaintext (`picoCTF`).


### Exploit
```
$ cat ciphertext.txt | python vigenere_cipher.py 
Key (cyclical): AGFLAGF
Key: AGFL
plaintext: picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_901e13a1}
```


### Hints
- There are tools that make this easy.
- This cipher was NOT invented by Pascal
