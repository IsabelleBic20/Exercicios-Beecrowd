casoTeste = int(input())
contador = 0
while contador < casoTeste:
  numero = int(input())
  divisor = 0
  for i in range(1, numero):
    if numero % i == 0:
      divisor += 1
  if divisor > 2:
    print(numero, "nao eh primo")
  else:
    print(numero, "eh primo")

  contador += 1
