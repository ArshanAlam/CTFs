cipher = str(input())

result = list()
a = ord('a')
A = ord('A')
NUM_CHARS = 26

for x in cipher:
    if x.islower():
        result.append(chr(a + ((ord(x)-a) + 13) % NUM_CHARS))
    elif x.isupper():
        result.append(chr(A + ((ord(x)-A) + 13) % NUM_CHARS))
    else:
        result.append(x)

print("".join(result))
