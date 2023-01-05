a = 1
b = 1

while a != 0 or b != 0:
  a, b = input().split()
  a = int(a)
  b = int(b)
  if a == 0 or b == 0:
    break
  maior = 0
  if a > b:
    maior = a
    a = b
    b = maior
    soma = 0
  for i in range(a, b + 1):
    soma += i
  print(i, "Sum=", soma)
  soma = 0

#So falta editar a saida mas a logica do codigo esta certa e os resultados batem!
