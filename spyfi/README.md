# SpyFi
James Brahm, James Bond's less-franchised cousin, has left his secure communication with HQ running, but we couldn't find a way to steal his agent identification code. Can you? Conect with `nc 2018shell.picoctf.com 31123`. [Source](spy_terminal_no_flag.py).


## Solution
After reviewing the given source code I knew that this problem involved exploiting the vulnerabilities of [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in [ECB mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)).

I found this [chosen plaintext attack](https://www.linkedin.com/pulse/short-note-prefix-chosen-plaintext-attack-cpa-ecb-mode-hannes-salin) article very helpful in writing my exploit.

Looking at the source code, we see that the application takes user input, encrypts it with the flag, and returns the encrypted message. Also, notice that the encrypted flag is returned with the message.

```
#!/usr/bin/python2 -u
from Crypto.Cipher import AES

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"
print welcome

sitrep = raw_input("Please enter your situation report: ")
message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( sitrep, agent_code )

message = pad(message)
print encrypt( """key""", message )
```

Also, notice that the block size is `16`. This is important because every identical block (of size 16 bytes), encrypted with the same key in ECB mode, would return an identical ciphertext block.

If you notice the message that this program is encrypting, it could be broken down into `3` main parts:

- Pre User Input
- User Input
- Post User Input


#### Pre User Input
The pre user input is the snippet of text below. It has length of 53 bytes. This also includes the `\n` newline characters.

```
Agent,
Greetings. My situation report is as follows:
```


#### User Input
The user input part varies and is controlled by the user.


#### Post User Input
The post user input portion includes some text and then the flag.

```
My agent identifying code is: {1}.
```


### Message Format
If I were to draw this out, it would look something like this:

```
|-------------------------------|---------------------------|-----------------------------------------------|------------------|
|         PRE USER INPUT      \n|          USER INPUT       |\n   THE BLOCK OF TEXT AFTER THE USER INPUT  \n|  FLAG            |
|-------------------------------|---------------------------|-----------------------------------------------|------------------|
                                ^                           ^                                               ^
                              53 bytes                    53 + size(user_input) bytes                53 + size(user_input) + 31 bytes
```


### Attack
The general idea behind the attack is to provide user input that would align the first character of the flag as the last character within the block before it. This could be achieved by sending user input with the appropriate size. Since we know the size of the message before the flag and the size of the user input, we could accurately determine the encrypted blocks within the ciphertext.

The first step is to pad the user input to end the `PRE USER INPUT` block. Since the pre user input block is of size `53` bytes then we need to provide `11` bytes of padding. The message follows the padding.

So for instance, if we would like to know what the encrypted block for `this_is_an_apple` (notice that the size of the message is 16 bytes), then we would send user input `AAAAAAAAAAAthis_is_an_apple`. By doing this, we know that the encrypted block for `this_is_an_apple` starts at byte `64` and ends at byte `80`.

why?

The encrypted block for the message starts at byte `64` because the `PRE USER INPUT` ends at byte `53` and the padding (of size 11 bytes) ends before byte `64`.

Also, since the block size is `16` we know that the ciphertext between byte `64` and byte `80` is correct.

Thus, we could code this up and write a function that takes arbitrary input and returns the encrypted blocks. We now have an encryption [oracle](https://en.wikipedia.org/wiki/Padding_oracle_attack).

By varying the padding size, we want to end up in a situation like this `block_0 = |My agent identi|` and `block_1 = |fying code is: X|`. Notice, the `X` in `block_1`. The `X` is the first character of the flag. We don't know what `X` is, but we know what the ciphertext looks like for it. Also, we know have a way to get ciphertext of arbitrarily blocks. Thus we could brute-force the character `X` by changing it to some printable ASCII character, encrypting that, and checking if the ciphertext is the same as the the ciphertext for `block_1`.

So I would use the oracle to encrypt `block_2 = |fying code is: A|` and get `ciphertext_2`. Then I would check if `ciphertext_2 == ciphertext_1` where `chipertext_1` is the ciphertext for `block_1`. If the ciphertext are equal, then we know that `X == A`.

We would add `A` to a `result` list, shift the block by `1` character and repeat.

So the next block we would test is `|ying code is: AX|`. Where `A` is the cracked part of the flag and `X` is what we are now trying to break.

I've implemented this entire attack in [crack_ecb.py](crack_ecb.py).


#### Flag
The flag is `picoCTF{@g3nt6_1$_th3_c00l3$t_6949075}`.


## Hints
- What mode is being used?
