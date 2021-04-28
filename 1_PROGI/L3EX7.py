#Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis, ao mesmo tempo,
#por 2 e 9

print('Apresenta os números que são divisíveis por 4 e 9')

i=1
number=[]

while i<=4:
    a=int(input('Digite um número: '))
    if a%4==0 and a%9==0:
        number.append(a)
    i=i+1
if len(number) != 0:
    print('Os numeros divisiveis por 4 e 9 simuntaneamnete sao', number)
else:
    print('Nenhum numero é divisivel por 4 e 9 simutaneamente')