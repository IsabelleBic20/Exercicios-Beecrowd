cont = 0
vetor = []
aux = 0
for i in range(10):
  num = int(input())
  vetor.append(num)
  
  for i in range(5):
    aux = vetor
    vetor.append(vetor[10-i])
    vetor[10-i]=aux
  print(f"N[{i}] = {vetor[i].reverse()}")

