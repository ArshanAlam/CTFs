# Solve this Caesar chipher by shifting the `input_str` 26 times.

input_str = input()


MAX_SHIFT_AMOUNT = 26
for shift_amount in range(MAX_SHIFT_AMOUNT):
  result = []

  for c in input_str:
    if (c.isalpha()):
      letter_case = "A" if c.isupper() else "a"
      c_num = ord(c) - ord(letter_case)
      c_shift_num = (c_num + shift_amount) % MAX_SHIFT_AMOUNT
      c_shifted_char = chr(c_shift_num + ord(letter_case))
      result.append(c_shifted_char)
    else:
      result.append(c)

  print("".join(result))


