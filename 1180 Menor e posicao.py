teste = int(input())
lista = []
numeros = list(map(int, input().split()))

for i in range(teste):
  lista.insert(i, numeros[i])
  menor = lista[0]

for i in range(teste):
  if lista[i] < menor:
    menor = lista[i]

print("Menor valor:", menor)
print("Posicao:", i)
