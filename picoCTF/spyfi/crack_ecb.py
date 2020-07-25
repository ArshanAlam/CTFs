import socket
import time

HOST="2018shell.picoctf.com"
PORT=31123
CIPHERTEXT_PRE_SIZE=53
CHARSET="UTF-8"
BLOCK_SIZE=16

# this flag size is an educated guess. It is a multiple of BLOCK_SIZE
# to ensure that the cracking algorithm functions correctly
FLAG_SIZE=BLOCK_SIZE * 4
BASE_PADDING_SIZE=11 + FLAG_SIZE


def oracle(msg):
  """
  Send the given message to the oracle so that it could be encrypted.
  Note: The message will also include other encrypted content
  """
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.sendall(msg.encode(CHARSET))
  s.shutdown(socket.SHUT_WR)
  result = list()
  while True:
    data = s.recv(4096)
    if not(data):
      break
    result.append(data)
  
  # The encrypted content is at the last index
  content = result[-1].decode(CHARSET)
  content_parts = content.strip().split()

  # the encrypted hex is at the last index of the contents parts
  encrypted_msg_str = content_parts[-1]
  return encrypted_msg_str



def pad(msg):
  """
  Make the message fit within blocks of size BLOCK_SIZE.
  """
  N = len(msg)

  if N % 16 == 0:
    return msg

  padding_amount = BLOCK_SIZE - (N % BLOCK_SIZE)
  return msg + ("0"*padding_amount)


def encrypt(msg, padding_size=BASE_PADDING_SIZE):
  """
  Encrypt the given message with the given padding size.
  """
  msg = pad(msg)
  N = len(msg)
  
  # we multiple by 2 because a single byte is 2 characters in hex (string representation)
  msg_start = (CIPHERTEXT_PRE_SIZE + padding_size) * 2

  # the adjusted message takes into account the size of the text that
  # comes before the message to ensure that it fits well into the block
  adjusted_msg = "A"*padding_size + msg
  ciphertext = oracle(adjusted_msg)
  return ciphertext[msg_start:msg_start + N * 2] 


def get_target(char_num):
  """
  Get the content of the target block. The target block is the
  block of the message we are currently trying to crack. The char_num
  is the character in the message that we are trying to break.
  Note: This function assumes that the target is always BLOCK_SIZE big.
  """
  padding_size = BASE_PADDING_SIZE - char_num
  # we multiple by 2 because a single byte is 2 characters in hex (string representation)
  target_start = (CIPHERTEXT_PRE_SIZE + BASE_PADDING_SIZE + BLOCK_SIZE) * 2
  ciphertext = oracle("A"*padding_size)
  return ciphertext[target_start:target_start + BLOCK_SIZE * 2]


def crack():
  result = list()

  # this is the 15-bytes before the flag - we're going to crack
  # the flag one character at a time
  orig_msg = "fying code is: "

  for size in range(FLAG_SIZE):
    target = get_target(size)
    # iterate over all possible printable ASCII characters
    for byte_num in range(32, 127):
      msg = str(orig_msg) + chr(byte_num)
      encrypted_msg = encrypt(msg)
      print(chr(byte_num), encrypted_msg, target, msg, result)
      if encrypted_msg == target:
        result.append(chr(byte_num))
        break
    
    # if we have cracked the entire flag then exit
    # the flag ends with a '}' and a period '.' since the
    # message would have the form "picoCTF{***}."
    if len(result) > 2 and result[-2] == "}" and result[-1] == ".":
      break

    # remove the front character in the block and add a 'hit' character at the end
    orig_msg = orig_msg[1:] + result[-1]

  return result

result = crack()
print()
print("".join(result))
