def totient(p, q):
  return (p - 1)*(q - 1)


def lcm(p, q):
  if p == 0 and q == 0:
    return 0
  else:
    return abs(p * q) // gcd(p, q)


def gcd(p, q):
  if p == 0 and q == 0:
    return 0
  elif p == 0:
    return q
  elif q == 0:
    return p
  else:
    while q != 0:
      p, q = q, p % q
    return p


def encrypt(plaintext, e, n):
  return pow(plaintext, e, n)


def egcd(a, b):
  old_s = 1
  s = 0
  old_t = 0
  t = 1
  old_r, r = a, b

  while r != 0:
    q = old_r // r
    old_r, r = r, old_r - q * r
    old_s, s = s, old_s - q * s
    old_t, t = t, old_t - q * t
  
  return old_r, old_s, old_t


def calculate_d(p, q, e):
  phi_n = totient(p, q)
  g, x, y = egcd(e, phi_n)

  if x < 0:
    return x + phi_n

  return x


def decrypt(ciphertext, d, n):
  return pow(ciphertext, d, n)


print("y")
q = int(input())
p = int(input())
print(p * q)

print("y")
p = int(input())
n = int(input())
print(n // p)


print("N")

print("y")
q = int(input())
p = int(input())
print(totient(p, q))

print("y")
plaintext = int(input())
e = int(input())
n = int(input())
print(encrypt(plaintext, e, n))

print("N")

print("y")
q = int(input())
p = int(input())
e = int(input())
print(calculate_d(p, q, e))


print("y")
p = int(input())
ciphertext = int(input())
e = int(input())
n = int(input())
q = n // p

potential_flag = decrypt(ciphertext, calculate_d(p, q, e), n)
print(potential_flag)
print(bytes.fromhex(hex(potential_flag)[2:]).decode("UTF-8"))
