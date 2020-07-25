ALPHA_SIZE = 26

# get the ciphertext from stdin
CIPHERTEXT = input()

"""
Generate the vigenere square.
"""
def get_vigenere_square():
  vigenere_square = list()
  for SHIFT in range(ALPHA_SIZE):
    cur_row = list()
    for letter in range(ALPHA_SIZE):
      cur_row.append(chr(ord('A') + ((SHIFT + letter) % ALPHA_SIZE)))
    vigenere_square.append(cur_row)
  return vigenere_square


vigenere_square = get_vigenere_square()

"""
Decrypt the given ciphertext with the given key.
"""
def decrypt(ciphertext, key):
  result = list()
  M = len(key)
  i = -1
  for x in ciphertext:
    if not(x.isalpha()):
      result.append(x)
      continue

    i += 1
    # get the index of the letter that corresponds to the plaintext
    idx = vigenere_square[ord(key[i % M].upper()) - ord('A')].index(x.upper())

    if x.isupper():
      result.append(chr(ord('A') + idx))
    else:
      result.append(chr(ord('a') + idx))
    
 
  return "".join(result)


"""
Generate a key with the given size
"""
def generate_key(size):
  if size <= 0:
    yield ""
  else:
    for i in range(ALPHA_SIZE):
      for key in generate_key(size - 1):
        yield chr(ord('A') + i) + key


"""
Given the ciphertext and the plaintext return the key.
"""
def get_key(ciphertext, plaintext):
  result = list()
  for c,p in zip(ciphertext, plaintext):
    for i in range(ALPHA_SIZE):
      row = vigenere_square[i]
      if row[ord(p.upper()) - ord('A')] == c.upper():
        result.append(row[0])
  return "".join(result)



"""
Crack the given ciphertext with using the given key size. The
crack is successful if the given success_token is in the cracked
plaintext.
"""
def crack(ciphertext, key_size, success_token):
  for key in generate_key(key_size):
    plaintext_candidate = decrypt(ciphertext, key)
    if success_token in plaintext_candidate:
      return (key, plaintext_candidate)


# Crack the flag, by getting the bruteforcing the key and decrypt the ciphertext using that key
key, plaintext = crack(CIPHERTEXT, 4, "picoCTF")
print("Key (cyclical):", get_key(CIPHERTEXT[:7], "picoCTF"))
print("Key:", key)
print("plaintext:", plaintext)
