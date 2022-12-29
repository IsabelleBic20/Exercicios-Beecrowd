n=int(input())

for t in range(n):
    x, y = map(int, input().split())

    if x%2==0:
        x=x+1
    soma=0
    for i in range(y)    :
        soma=soma+x
        x=x+2

    print(soma)  