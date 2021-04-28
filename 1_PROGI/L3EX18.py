# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

print('Este app mostra os valores em ordem crescente')

n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))

if n1>n2:
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1

print (menor, maior)