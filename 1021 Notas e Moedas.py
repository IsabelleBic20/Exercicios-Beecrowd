dinheiro = float(input())

d100 = int(dinheiro / 100)
dinheiro = dinheiro % 100

d50 = int(dinheiro / 50)
dinheiro = dinheiro % 50

d20 = int(dinheiro / 20)
dinheiro = dinheiro % 20

d10 = int(dinheiro / 10)
dinheiro = dinheiro % 10

d5 = int(dinheiro / 5)
dinheiro = dinheiro % 5

d2 = int(dinheiro / 2)
dinheiro = dinheiro % 2

#MOEDA

m1 = int(dinheiro / 1)
dinheiro = dinheiro % 1

m5 = int(dinheiro / 0.5)
dinheiro = dinheiro % 0.5

m25 = int(dinheiro / 0.25)
dinheiro = dinheiro % 0.25

m10 = int(dinheiro / 0.10)
dinheiro = dinheiro % 0.10

m05 = int(dinheiro / 0.05)
dinheiro = dinheiro % 0.05

m001 = int(dinheiro / 0.01)
dinheiro = dinheiro % 0.01

print("NOTAS:")
print(d100, "nota(s) de R$ 100.00")
print(d50, "nota(s) de R$ 50.00")
print(d20, "nota(s) de R$ 20.00")
print(d10, "nota(s) de R$ 10.00")
print(d5, "nota(s) de R$ 5.00")
print(d2, "nota(s) de R$ 2.00")

print("MOEDAS:")
print(m1, "moeda(s) de R$ 1.00")
print(m5, "moeda(s) de R$ 0.50")
print(m25, "moeda(s) de R$ 0.25")
print(m10, "moeda(s) de R$ 0.10")
print(m05, "moeda(s) de R$ 0.05")
print(m001, "moeda(s) de R$ 0.01")
