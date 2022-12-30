a = int(input())
b = int(input())
soma = 0
if a < b:
  for i in range(a, b):
    if i % 13 != 0:
      soma += i

if b < a:
  for i in range(b, a):
    if i % 13 != 0:
      soma += i

print(soma)
