maior = 0
soma = 0
n = int(input())
for j in range(n):
  a, b = input().split()
  a = int(a)
  b = int(b)
  #ordenando em ordem crescente
  if a > b:
    maior = a
    a = b
    b = maior
  for i in range(a + 1, b):
    if i % 2 != 0:
      soma += i

  print(soma)
  soma = 0  #zerando a variavel de soma a cada loop, se nao fizer isso ele vai somar todos os impares juntos
