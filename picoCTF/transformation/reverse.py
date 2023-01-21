import sys

def reverse(utf8_str: str) -> str:
  result = list()

  for c in utf8_str:
    # Get the UTF-8 character number
    c_ord = ord(c)

    # Each UTF-8 character contains (first, second) two ASCII character
    # that belong to the flag. The first ASCII character of the flag
    # could be reversed by bit shifting to the right by 8 bits.
    # Notice that is the opposite bit shift direction of the encoding algorithm.
    first = c_ord >> 8

    # To get the second ASCII character we could do some basic math
    # by rearrange the equation from the encoding algorithm.
    second = c_ord - (first << 8)

    result.append(chr(first))
    result.append(chr(second))

  return "".join(result)


if __name__ == "__main__":
  print(reverse(input())) 