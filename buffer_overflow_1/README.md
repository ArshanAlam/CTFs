# Buffer Overflow 1
Okay now you're cooking! This time can you overflow the buffer and return to the flag function in this program?

## Solution
The input buffer is 40 bytes below the frame pointer, and right above the frame pointer is the return address. Thus, by inputing `echo -ne "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\xcb\x85\x04\x08" | ./vuln` we overflow the buffer and set the return address to the `win()` function that prints the flag. I used [radare2](https://github.com/radareorg/radare2) to get the address of `win()`, which is `0x080485cb`. Than I carefully crafted the input so that the return address is updated to be the address of win. Notice how the bytes of the return address in the input string are backwards. This is because of the way the [endianness](https://en.wikipedia.org/wiki/Endianness).
