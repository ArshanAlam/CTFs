# Use binary search to find the nth root
def find_nth_root(m, n):
  high = 1
  while high ** n < m:
    high *= 2

  low = high // 2
  while low < high:
    mid = (low + high) // 2
    if mid ** n < m:
      low = mid + 1
    else:
      high = mid - 1

  return low



n = int(input())
e = int(input())
c = int(input())

k = 0

# m = (c + k*n)^(1/e)
m = find_nth_root(c + (k*n), e)

m_ascii = m.to_bytes(length=m.bit_length(), byteorder="big").decode("UTF-8")
print(m_ascii)
