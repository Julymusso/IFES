# Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando
# se o número é par ou ímpar.

print('Este app identifica se o numero é par ou impar')

a=int(input('Digite um número: '))

if a%2==0:
    print ('Este numero e PAR')
else:
    print('Este numero e IMPAR')