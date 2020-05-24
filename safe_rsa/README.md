# Safe RSA
Now that you know about RSA can you help us decrypt this [ciphertext](ciphertext)? We don't have the decryption key but something about those values looks funky..


## Solution
Looking at the given ciphertext we immediately notice that `e` is small. We know that `c = (m**e) % n`. This means that `m**e = (c + k*n)` for some value `k`. After some experimentation I discovered that `k = 0`. Thus the problem reduces down to solving `c**(1/e)`. However, using Python to solve for `m = c ** (1/e)` was not good enough because we lose precision. Thus, I wrote a function that calculates the *Nth* root using [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm).


```
# Use binary search to find the nth root
def find_nth_root(m, n):
  high = 1
  while high ** n < m:
    high *= 2

  low = high // 2
  while low < high:
    mid = (low + high) // 2
    if mid ** n < m:
      low = mid + 1
    else:
      high = mid - 1

  return low



n = int(input())
e = int(input())
c = int(input())

k = 0

# m = (c + k*n)^(1/e)
m = find_nth_root(c + (k*n), e)

m_ascii = m.to_bytes(length=m.bit_length(), byteorder="big").decode("UTF-8")
print(m_ascii)
```


### Exploit
Therefore the exploit becomes:


```
$ cat ciphertext_clean | python cube_root_attack.py 
picoCTF{e_w4y_t00_sm411_a5b5aaac}
```


## Hints
- [RSA tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- Hmmm that `e` value looks kinda small right?
- These are some really big numbers.. Make sure you're using functions that don't lose any precision!
