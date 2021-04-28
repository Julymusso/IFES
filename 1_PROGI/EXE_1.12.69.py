original=1
while original!=0:
    numberBase3=int(input("Insira um número de base 3:"))
    original=numberBase3
    cont=0
    decimal=0
    if numberBase3!=0:
        while numberBase3>0:
            algarismo=numberBase3%10
            valor=(3**cont)*algarismo
            numberBase3=numberBase3//10
            decimal=decimal+valor
            cont=cont+1

        print("Base 3:",original,"\nBase 10:",decimal)

