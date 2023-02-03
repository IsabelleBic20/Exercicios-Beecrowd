num = int(input())
soma = 0
numeros = list(map(int, input().split()))

for i in range(len(numeros)):
  if numeros[i] == num:
    soma += 1

print(soma)
