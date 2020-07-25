# Caesar Cipher 2

Can you help us decrypt this [message](ciphertext)? We believe it is a form of a [caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). You can find the ciphertext in /problems/caesar-cipher-2_3_4a1aa2a4d0f79a1f8e9a29319250740a on the shell server.


## Solution
I wrote a script that applies a shift to all printable ASCII characters. One of those shifts resulted in a valid decryption of the flag.


```
cat ciphertext | python decrypt_caesar.py | grep -o "picoCTF{.*}"
```


## Hints
- You'll have figure out the correct alphabet that was used to encrypt the ciphertext from the ascii character set
- [ASCII Table](https://www.asciitable.com/)
