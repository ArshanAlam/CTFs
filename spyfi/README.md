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
"""Agent,
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

The first step is to padd the user input to end the `PRE USER INPUT` block. Since the pre user input block is of size `53` then we need to provide `11` bytes plus the message in our user input.

So for instance, if we would like to know what the encrypted block for `this_is_an_apple` (notice that the size of the message is 16 bytes), then we would send user input `AAAAAAAAAAAthis_is_an_apple`. Do this, we know that the encrypted block for `this_is_an_apple` starts at byte `64` and ends at byte `80`.


## Hints
- What mode is being used?
