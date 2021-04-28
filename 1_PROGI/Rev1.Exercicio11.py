data = int(input("Digite uma data no formato DDMMAA: "))

D = data//100000
data = data%100000
D = (D*10) + (data//10000)
data = data%10000

M = data//1000
data = data%1000
M = (M*10) + (data//100)
data = data%100

A = data//10
A = A*10 + (data%10)

data = A*10000 + M*100 + D

print (data)
