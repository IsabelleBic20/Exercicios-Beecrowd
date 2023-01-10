num_caso = int(input())
j = 0
while j < num_caso:
  numero = int(input())
  conta = 0
  for i in range(1, numero):
    if numero % i == 0:
      conta += i
  if numero == conta:
    print(numero, "eh perfeito")
  else:
    print(numero, "não eh perfeito")
j += j
