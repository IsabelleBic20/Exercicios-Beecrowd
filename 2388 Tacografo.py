n = int(input())
distanciatotal = 0
for i in range(n):
  tempo, vm = input("").split()
  tempo = int(tempo)
  vm = int(vm)
  distanciatotal += tempo * vm
print(distanciatotal)