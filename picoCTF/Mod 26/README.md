# Mod 26

Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}`

# Solution

The flag, given in the problem description, is encrypted using [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). To solve this problem, I wrote a simple Python program that executes `26` shifts of the given input and prints the result. Next, we `grep` for any line that contains `picoCTF`.

```
$ echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}" | python solve_caesar_cipher.py | grep 'picoCTF'
```

<details>

<summary>Flag</summary>

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}
```

</details>
