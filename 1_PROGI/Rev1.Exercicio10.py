N = int(input("Digite um número :"))
C = N // 100
N = N % 100
D = N // 10
U = N % 10

M = U*100 + D*10 + C

print (M)