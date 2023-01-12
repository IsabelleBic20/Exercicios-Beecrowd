x = []
for i in range(1, 11):
  num = int(input())
  x.append(num)

for j in range(len(x)):
  if x[j] <= 0:
    x[j] = 1
  print(f"X[{j}] = {x[j]}")