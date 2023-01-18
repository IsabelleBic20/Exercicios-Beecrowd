n = int(input())
vet = []
for i in range(1000):
  soma = 0
  while soma < n:
    vet.append(soma)
    soma += 1
  print(f"N[{i}] = {vet[i]}")