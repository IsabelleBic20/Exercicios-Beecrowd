num = int(input())
x = []
i = 0

while i < 10:
  x.append(num)
  num = num * 2
  print(f"N[{i}] = {x[i]}")
  i = i + 1
