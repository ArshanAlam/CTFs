def totient(p, q):
  return (p - 1)*(q - 1)


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

p = int(input())
q = int(input())
c = int(input())
n = int(input())
e = int(input())

m = pow(c, calculate_d(p, q, e), n)
m_ascii = m.to_bytes(length=m.bit_length(), byteorder="big").decode("UTF-8")
print(m_ascii)
