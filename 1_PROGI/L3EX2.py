# Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um valor
# positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se de verificar
# se o número fornecido é menor que zero; sendo, multiplique-o por –1.

print('Este app calcula o módulo de um número inteiro')
num=int(input('Digite um número: \n'))

if num>= 0:
    num2=num
else:
    num2=num*(-1)
print ('O módulo de',num,'é',num2)