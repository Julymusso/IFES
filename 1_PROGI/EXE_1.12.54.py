numAproximacao=20

y=float(input("Insira o número que deseja obter a raiz quadrada: "))
x=y/2
for i in range (1,numAproximacao):
    x=((x*x)+y)/(2*x)

print("A raíz quadrada de",y,"é {:.1f}".format(x))