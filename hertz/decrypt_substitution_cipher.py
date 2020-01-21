NUM_CHARS = 26
FILENAME = "ciphertext"

ENG_LETTER_FREQ = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "u", "w", "m", "f", "c", "g", "y", "p", "b", "k", "v", "j", "x", "q", "z"]

ENG_BIGRAM_FREQ = ["th", "he", "in", "er", "an", "re", "nd", "on", "en", "at", "ou", "ed", "ha", "to", "or", "it", "is", "hi", "es", "ng"]

ENG_TRIGRAM_FREQ = ["the", "and", "ing", "her", "hat", "his", "tha", "ere", "for", "ent", "ion", "ter", "was", "you", "ith", "ver", "all", "wit", "thi", "tio"]


# Done manually after using data from frequency analysis
# ciphertext -> UPPER(plaintext)
SUBSTITUTION = {"g": "E", "l": "T", "e": "H", "w": "N", "a": "A", "h": "D", "m": "I", "q": "G", "k": "S", "v": "U", "u": "B", "n": "O", "d": "C", "j": "P", "s": "R", "i": "Y", "z": "F", "b": "L", "y": "V"}

def read_file(filename):
    return open(filename, "r", encoding="utf-8").read()


def apply_substitution(content):
    result = []
    for x in content:
        if x.isalpha():
          if x in SUBSTITUTION:
            result.append(SUBSTITUTION[x])
          else:
            result.append(x)
        else:
            result.append(x)
    return "".join(result)


def order_frequency(freq):
    sorted_freq = sorted(freq.items(), key=lambda item:  item[1], reverse=True)
    return sorted_freq


def count_frequency(content):
    freq = dict()
    for x in content:
        if x.isalpha():
            if x not in freq:
                freq[x] = 0
            freq[x] += 1
    return freq


def count_bigram(content):
  freq = dict()
  prev = None
  for x in content:
    if x.isalpha() and prev:
      key = prev + x
      if key not in freq:
        freq[key] = 0
      freq[key] += 1
      
    # ignore all non alphabetical characters, also ignore
    # characters that don't come in pair
    if x.isalpha():
      prev = x
    else:
      prev = None

  return freq

      
def count_trigram(content):
  freq = dict()
  prev_1 = None
  prev_2 = None
  for x in content:
    if x.isalpha() and prev_1 and prev_2:
      key = prev_1 + prev_2 + x
      if key not in freq:
        freq[key] = 0
      freq[key] += 1
      
    # ignore all non alphabetical characters, also ignore
    # characters that don't come in pair
    if x.isalpha():
      prev_1, prev_2 = prev_2, x
    else:
      prev_1 = None
      prev_2 = None

  return freq



def break_cipher():
    content = read_file(FILENAME)
    #print(content)

    freq = count_frequency(content)
    ord_freq_list = order_frequency(freq)
    print(ENG_LETTER_FREQ)
    print("Ordered frequency", ord_freq_list, "\n")

    
    bigram_freq = count_bigram(content)
    ord_bigram_list = order_frequency(bigram_freq)
    print(ENG_BIGRAM_FREQ)
    print("Ordered bigram", ord_bigram_list[:20], "\n")

    trigram_freq = count_trigram(content)
    ord_trigram_list = order_frequency(trigram_freq)
    print(ENG_TRIGRAM_FREQ)
    print("Ordered trigram", ord_trigram_list[:20], "\n")
    
    # apply the substitution
    result = apply_substitution(content)
    print(result)
    
    print()
    print("Flag is =", "SUBSTITUTION_CIPHERS_ARE_SOLVABLE_CDILGNDLNP".lower())
    print()


break_cipher()
