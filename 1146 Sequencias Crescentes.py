n = 1
while n != 0:
  n = input("")
  n = int(n)
  if n == 0:
    break
  else:
    for i in range(1, n + 1):
      print(i, end=" ")
      
