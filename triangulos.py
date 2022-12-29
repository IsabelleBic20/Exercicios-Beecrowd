x, y, z = input().split()
a = float(x)
b = float(y)
c = float(z)

maior = 0

if a < b + c and b < c + a and c < a + b:
  perimetro = a + b + c
  print("Perimetro =", perimetro)
else:
  area = ((a + b) * c) / 2
  print("Area =", area)