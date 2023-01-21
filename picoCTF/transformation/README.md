# Transformation

I wonder what this really is... [enc](enc)

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hints

* You may find some decoders online

### Solution

After downloading the [enc](enc) file, I immediately executed the `file` command on it.

```shell
$ file enc 
enc: UTF-8 Unicode text, with no line terminators
```

The `file` command mentioned that it's a [UTF-8](https://en.wikipedia.org/wiki/UTF-8) text file. Printing the file outputted non-[ASCII](https://en.wikipedia.org/wiki/ASCII) characters.


```shell
$ cat enc 
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸
```

Thus, we'll have to reverse engineer these UTF-8 characters back into the ASCII flag. Reviewing the encoding algorithm `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])` it became clear that each UTF-8 character has two ASCII characters encoded within it.


Luckily, [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 3+ uses UTF-8 as the default character encoding. Hence, I wrote a script that read the [enc](enc) file from [stdin](https://en.wikipedia.org/wiki/Standard_streams), extracted the ASCII characters from each UTF-8 character, then concatenated the result.

```python
import sys

def reverse(utf8_str: str) -> str:
  result = list()

  for c in utf8_str:
    # Get the UTF-8 character number
    c_ord = ord(c)

    # Each UTF-8 character contains (first, second) two ASCII character
    # that belong to the flag. The first ASCII character of the flag
    # could be reversed by bit shifting to the right by 8 bits.
    # Notice that is the opposite bit shift direction of the encoding algorithm.
    first = c_ord >> 8

    # To get the second ASCII character we could do some basic math
    # by rearrange the equation from the encoding algorithm.
    second = c_ord - (first << 8)

    result.append(chr(first))
    result.append(chr(second))

  return "".join(result)


if __name__ == "__main__":
  print(reverse(input())) 
```

Running the script above, on the encoded file, results in the flag.

```shell
$ cat enc | python reverse.py 
picoCTF{16_bits_inst34d_of_8_75d4898b}
```



#### Flag

```
picoCTF{16_bits_inst34d_of_8_75d4898b}
```
