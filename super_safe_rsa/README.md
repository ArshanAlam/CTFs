# Super Safe RSA
Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with `nc 2018shell.picoctf.com 59208`.

## Solution
Notice that `n`, from netcat, is small. It is 80-digits long. Thus, we should be able to prime factor this integer.

```
$ nc 2018shell.picoctf.com 59208
c: 3616181649900121141799314742290204950868710639390854925393756780276445635300775
n: 14934514563878404182198028605990879517958048155819405847673073509001764041553203
e: 65537
```

I used [this](https://www.alpertron.com.ar/ECM.HTM) website to factor `n` into `p` and `q` such that `n = p × q`. We get,
```
13 231152 475495 176840 422490 383927 141160 477227 542803 949884 384202 492217 661181 506791 (80 digits) = 141 777522 766828 535658 576720 964858 998037 (39 digits) × 93323 343625 177578 611970 641071 834603 237643 (41 digits)
```

Thus,
```
p = 141777522766828535658576720964858998037
q = 93323343625177578611970641071834603237643
```

How that we have the prime factors, we could determine the [private key](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation) using the [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).

### Exploit
The full exploit becomes:

```
$ cat factors.txt clean_input.txt | python small_prime_attack.py 
picoCTF{us3_l@rg3r_pr1m3$_3432}
```


## Hints
- Just try the first thing that comes to mind.
