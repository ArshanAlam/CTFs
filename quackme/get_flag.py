greeting_msg = "You have now entered the "
sekrut_buffer = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x5c\x10\x06\x06\x18\x45\x51\x00\x5d\x00"
result_input = bytes(ord(a)^ord(b) for a,b in zip(greeting_msg, sekrut_buffer))
print(result_input)
