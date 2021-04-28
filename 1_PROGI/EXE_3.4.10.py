def algarismo(num):
    cont=0
    while num>1:
        num=num/10
        cont=cont+1
    return cont

def separar(num,qtdAlgarismo):
    for i in range (1,qtdAlgarismo+1):
        a=num%10
        num=num//10
        return a

def inverter(num,qtdAlgarismo):
    numInvertido=0
    while qtdAlgarismo>=0:
        numInvertido=numInvertido+num*(10**qtdAlgarismo-1)
        qtdAlgarismo=qtdAlgarismo-1
        return numInvertido


a=int(input("Insira um número: "))
print(algarismo(a))
#numeroInvertido=inverter(separar(a,algarismo(a)),algarismo(a))
#print(numeroInvertido)