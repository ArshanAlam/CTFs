def words_to_ascii(words: list[str]) -> list[str]:
  result = list()

  for word in words:
    char_list = list()
    for i in range(0, 8, 2):
      hex_str = "0x{}{}".format(word[i], word[i+1])
      byte_decimal_value = int(hex_str, 16)
      char_list.append(chr(byte_decimal_value))

    # We reverse the cur_str because x86 is little endian
    char_list.reverse()

    result.append("".join(char_list))

  return result


if __name__ == "__main__":
  raw_word_str = input()
  words = [word.strip() for word in raw_word_str.split(".")]
  words = list(filter(lambda word: len(word) == 8, words))

  print("".join(words_to_ascii(words)))
