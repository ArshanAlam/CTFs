# Python Wrangling

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](ende.py) using this [password](pw.txt) to get the [flag](flag.txt.en)?


## Hints
1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py`
1. `$ man python`


### Solution
The given Python script encrypts and decrypts the content of a file using a user provided password. To get the flag, we pipe the provided password into the script and grep for the flag.

```
cat pw.txt | python ende.py -d flag.txt.en | grep -o 'picoCTF{.*}'
```
