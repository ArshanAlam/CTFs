# read the input, convert it into a string, split the string
# on whitespaces, strip each token
token_list = [p.strip() for p in str(input()).split()]

# The final output
result = list()

BLOCK_SIZE=2
# for each token print the bytes in that token
for token in token_list:
  byte_list = [token[i:i+BLOCK_SIZE] for i in range(0, len(token), BLOCK_SIZE)]

  # due to endianness we need to reverse the bytes in the token 
  byte_list.reverse()

  # try to print the bytes as characters
  possible_ascii = list()
  for b in byte_list:
      possible_ascii.append(chr(int("0x"+b, 16)))

  result.append("".join(possible_ascii))

# print the final result
print("".join(result))
