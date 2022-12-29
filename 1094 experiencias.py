#EXPERIÊNCIAS

#Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

#Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

#Entrada
#A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

#Saída
#Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

#Entrada                  #Saída
#10                    #Total: 92 cobaias
#10 C                  #Total de coelhos: 29
#6 R                   #Total de ratos: 40
#15 S                  #Total de sapos: 23
#5 C                   #Percentual de coelhos: 31.52 %
#14 R                  #Percentual de ratos: 43.48 %
#9 C                   #Percentual de sapos: 25.00 %
#6 R
#8 S
#5 C
#14 R

n = int(input())
i = 0
total = 0
totalCoelhos = 0
totalSapos = 0
totalRatos = 0
percentualRatos = 0
percentualSapos = 0
percentualCoelhos = 0

for i in range(n):
  quantia, especie = input().split()
  quantia_int = int(quantia)
  if especie == 'C':
    totalCoelhos += quantia_int
  if especie == 'R':
    totalRatos += quantia_int
  if especie == 'S':
    totalSapos += quantia_int

total += totalCoelhos + totalRatos + totalSapos
percentualCoelhos = (totalCoelhos * 100) / total
percentualRatos = (totalRatos * 100) / total
percentualSapos = (totalSapos * 100) / total

print("Total:", total, "cobaias")
print("Total de coelhos:", totalCoelhos)
print("Total de ratos:", totalRatos)
print("Total de sapos:", totalSapos)
print(f"Percentual de coelhos: {percentualCoelhos:.2f} %")
print(f"Percentual de ratos: {percentualRatos:.2f} %")
print(f"Percentual de sapos: {percentualSapos:.2f} %")
