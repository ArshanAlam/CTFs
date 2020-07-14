printable_ascii = open("printable_ascii.txt", "r").read().strip()
printable_ascii_ciphertext = open("printable_ascii_ciphertext.txt", "r").read().strip().split()
flag_ciphertext = open("flag_ciphertext.txt", "r").read().strip().split()

ciphertext_to_ascii_map = dict()

N = len(printable_ascii)

for i in range(N):
  a = printable_ascii[i]
  c = printable_ascii_ciphertext[i]
  ciphertext_to_ascii_map[c] = a

flag = list()
for c in flag_ciphertext:
  flag.append(ciphertext_to_ascii_map[c])

print("".join(flag))
