v = []
for i in range(0, 100):
  x = float(input())
  v.append(x)

for j in range(len(v)):
  if v[j] <= 10:
    print(f"A[{j}] = {v[j]}")