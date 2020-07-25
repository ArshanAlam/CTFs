# Hertz 2
This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with `nc 2018shell.picoctf.com 18990`.


## Solution
This was a simple [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) that could be broken using [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis).

### Exploit
```
$ python decrypt_substitution_cipher.py 
ENG_LETTER_FREQ ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'w', 'm', 'f', 'c', 'g', 'y', 'p', 'b', 'k', 'v', 'j', 'x', 'q', 'z']
Ordered frequency [('e', 19), ('s', 15), ('k', 15), ('q', 14), ('o', 14), ('v', 12), ('n', 8), ('x', 8), ('l', 7), ('y', 7), ('w', 7), ('i', 6), ('f', 6), ('h', 5), ('t', 5), ('a', 5), ('u', 5), ('g', 4), ('b', 4), ('j', 3), ('d', 2), ('p', 2), ('c', 1), ('m', 1), ('r', 1), ('z', 1)] 

['th', 'he', 'in', 'er', 'an', 're', 'nd', 'on', 'en', 'at', 'ou', 'ed', 'ha', 'to', 'or', 'it', 'is', 'hi', 'es', 'ng']
Ordered bigram [('le', 4), ('sy', 3), ('nk', 3), ('ge', 3), ('en', 3), ('vl', 3), ('eo', 3), ('oq', 3), ('ne', 3), ('kp', 2), ('xo', 2), ('ow', 2), ('sq', 2), ('qh', 2), ('qf', 2), ('in', 2), ('kt', 2), ('tx', 2), ('xe', 2), ('eu', 2)] 

['the', 'and', 'ing', 'her', 'hat', 'his', 'tha', 'ere', 'for', 'ent', 'ion', 'ter', 'was', 'you', 'ith', 'ver', 'all', 'wit', 'thi', 'tio']
Ordered trigram [('vle', 2), ('eoq', 2), ('oqf', 2), ('ink', 2), ('nkt', 2), ('ktx', 2), ('txe', 2), ('xeu', 2), ('syk', 2), ('Vle', 1), ('chs', 1), ('hsy', 1), ('syd', 1), ('tnk', 1), ('nkp', 1), ('kpw', 1), ('akm', 1), ('rhu', 1), ('hui', 1), ('uiq', 1)] 

Ignore Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG. I CAN'T BELIEVE THIS IS SUCH AN EASY PROBLEM IN PICO. IT'S ALMOST AS IF I SOLVED A PROBLEM ALREADY! OKAY, FINE. HERE'S THE FLAG: PICOCTF{SUBSTITUTION_CIPHERS_ARE_TOO_EASY_DNGAOWMVYE}

Keep Case: The quick brown fox jumps over the lazy dog. I can't believe this is such an easy problem in Pico. It's almost as if I solved a problem already! Okay, fine. Here's the flag: picoCTF{substitution_ciphers_are_too_easy_dngaowmvye}
```
