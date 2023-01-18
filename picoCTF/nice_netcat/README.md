# Nice netcat...

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...


## Hints

1. what's a [netcat](https://en.wikipedia.org/wiki/Netcat)?
1. Reading and writing [ASCII](https://en.wikipedia.org/wiki/ASCII).


### Solution

After executing `nc mercury.picoctf.net 7449` I noticed that the output was a list of numbers that are within the ASCII range.

```shell
$ nc mercury.picoctf.net 7449
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
50 
100 
55 
99 
97 
102 
97 
125 
10 
```

![ASCII Table](ASCII-Table.svg)


Thus, I wrote a simple python utility that reads all the numbers from `stdin` into an array then converts each number into an ASCII character.

```python
# nums_to_ascii.py

import sys

def nums_to_ascii(num_array: list[int]) -> str:
  return "".join(chr(num) for num in num_array)


if __name__ == "__main__":
  num_array = [int(num) for num in sys.stdin]
  
  print(nums_to_ascii(num_array))
```

We find the flag by [piping](https://en.wikipedia.org/wiki/Pipeline_(Unix)) the output from netcat to the `nums_to_ascii.py` script.

```shell
# Write the output from netcat to a file
$ nc mercury.picoctf.net 7449 > nc_output.txt

# pipe the netcat output to nums_to_ascii.py
$ cat nc_output.txt | python nums_to_ascii.py 
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
```


#### Flag

```
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
```
