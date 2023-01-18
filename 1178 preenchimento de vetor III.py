num = float(input())
vet = []
for i in range(100):
  if i == 0:
    v = num
    vet.append(num)
  else:
    num = num / 2
    vet.append(num)
  print(f"N[{i}] = {vet[i]:.4f}")