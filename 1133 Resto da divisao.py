x = input()
y = input()

x = int(x)
y = int(y)

if x > y:
  maior = x
  x = y
  y = maior
for i in range(x + 1, y):
  if i % 5 == 2 or i % 5 == 3:
    print(i)