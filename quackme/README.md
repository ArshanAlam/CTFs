# Quack Me
Can you deal with the Duck Web? Get us the flag from the program in this directory.

## Solution
I used [Ghidra](https://ghidra-sre.org/) to disassemble this binary. In there I discovered that the application expected a carefully crafted input string which had the property `greeting_msg == input_str ^ sekrut_buffer`. Where `greeting_msg` is the message that is printed by the binary, and `sekrut_buffer` is a non-printed buffer in the binary.

Using Ghidra, I figured out what the bytes are for that buffer and than I wrote a python script that does the inverse operation to give me the `input_str`. So `input_str == greeting_msg ^ sekrut_buffer`. Turns out that the input string is the flag.
