import sys

def nums_to_ascii(num_array: list[int]) -> str:
  return "".join(chr(num) for num in num_array)


if __name__ == "__main__":
  num_array = [int(num) for num in sys.stdin]
  
  print(nums_to_ascii(num_array))

  
