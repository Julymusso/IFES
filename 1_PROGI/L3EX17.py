# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print('Este app informa se voce pode ou não votar esse ano')

n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))

if n1>n2:
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1

print ("O Maior e: "+str(maior)+" e o Menor e: "+str(menor))