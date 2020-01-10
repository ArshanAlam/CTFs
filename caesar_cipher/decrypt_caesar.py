ciphertext = input()

NUM_CHARS = 26
for shift in range(NUM_CHARS):
    cur = list()
    for x in ciphertext:
        cur.append(chr(ord('a') + ((ord(x) + shift) % NUM_CHARS)))
    print(shift, "=", "".join(cur))

