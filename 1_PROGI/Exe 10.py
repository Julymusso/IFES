#var
    #num, cont, soma: inteiro

cont=1
soma=0
while cont <= 10:
    num=int(input("Digite um número: "))
    if num<40:
        soma=soma+num
    cont=cont+1
print(soma)
