#var
    #num, cont, neg: inteiro

cont=1
neg=0
while cont <= 10:
    num=int(input("Digite um número: "))
    if num<0:
        neg=neg+1
    cont=cont+1
print(neg)
