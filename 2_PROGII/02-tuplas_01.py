
lista = [("Jorge",4,1500),("Elias",33,1200),("Pedro",22,3000),("Simaria",33,1400)]

def Bonus (lista):
    maiorTempo=0
    
    for (nome,meses,salario) in lista:
        if meses>maiorTempo:
            maiorTempo=meses

    for (nome,meses,salario) in lista:
        if meses==maiorTempo:
            print (nome,salario*1.1)

Bonus(lista)