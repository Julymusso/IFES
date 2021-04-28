#EEfetuar a leitura de cinco números inteiros e identificar o maior e o menor valor

print('Este app identifica o maior e o menor valor dentre 5')

i=1

while i<=5:
    a=int(input('Digite um número: '))
    if i==1:
        maior=a
        menor=a
    if i>1:
        if a>maior:
            maior=a
        elif a<menor:
            menor=a
    i=i+1
else:
    print('Menor: '+str(menor)+'\n'+'Maior: '+str(maior))