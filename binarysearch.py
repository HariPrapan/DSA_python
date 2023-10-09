def binary_search(L, v):
  if len(L) == 0:
    return False
  mid = len(L) // 2
  if v == L[mid]:
    return True
  elif v < L[mid]:
    return binary_search(L[:mid], v)
  else:
    return binary_search(L[mid + 1:], v)

# L is a sorted list
m = []
for i in range(1000000):
  m.append(i)

print("List made")

print(binary_search(m, 55555555555555))
