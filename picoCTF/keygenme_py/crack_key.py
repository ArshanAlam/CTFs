import hashlib

def crack_dynamic(username: bytes) -> str:
  result = list()
  hash_dex_digest = hashlib.sha256(username).hexdigest()

  result.append(hash_dex_digest[4])
  result.append(hash_dex_digest[5])
  result.append(hash_dex_digest[3])
  result.append(hash_dex_digest[6])
  result.append(hash_dex_digest[2])
  result.append(hash_dex_digest[7])
  result.append(hash_dex_digest[1])
  result.append(hash_dex_digest[8])

  return "".join(result)


if __name__ == "__main__":
  key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
  cracked_dynamic_part = crack_dynamic(b"SCHOFIELD")
  key_part_static2_trial = "}"

  key = "{}{}{}".format(key_part_static1_trial, cracked_dynamic_part, key_part_static2_trial)
  print(key)