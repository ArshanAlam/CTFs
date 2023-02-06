# Mind your Ps and Qs

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](values)


## Hints

1. Bits are expensive, I used only a little bit over 100 to save money


### Solution

After downloading the file [values](values), I immediately executed the `file` command on it.

```shell
$ file values 
values: ASCII text
```

Considering that the file is [ASCII](https://en.wikipedia.org/wiki/ASCII) characters, we could print the content using `cat`.

```shell
$ cat values 
Decrypt my super sick RSA:
c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537
```

Seeing that the content mentions [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption), I looked up how the RSA alogrithm does encryption and decryption.


#### RSA explained

* `e` and `n` are the public key
* `d` is the private key
* `M` is the cleartext message
* `C` is the ciphertext

```
(M^e)^d ≡ (M^d)^e ≡ M (mod n)
```

Thus, to encrypt `M` we use [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation) to solve:

```
C ≡ M^e (mod n)
```

To decrypt `C` we solve:

```
M ≡ C^d ≡ (M^e)^d ≡ M (mod n)
```

Considering that `n` is small, we could use [this](https://www.dcode.fr/rsa-cipher) online tool to decrypt the ciphertext. Using this tool we were able to get the flag. 


#### Flag

```
picoCTF{sma11_N_n0_g0od_73918962}
```