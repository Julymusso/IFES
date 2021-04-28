# Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de
# segundograu, apresentando as duas raízes, se para os valores informados for possível efetuar o referido
# cálculo. Lembre-se de que a variável A deve ser diferente de zero
import math

print('Este app cálcula as raízes da equação de segundo grau, dados valores "A","B" e "C".')

a=0
while a==0:
    a=float(input('Insira o valor de "A". (Acompanha o "X²"). Tem que ser diferente de "0": '))

b=float(input('Insira o valor de "B". (Acompanha o "X"): '))
c=float(input('Insira o valor de "C". (Não acompanhado): '))

try: #ajustar para caso delta retorne valor negativo
    delta=math.sqrt((b*b)-(4*a*c))
    r1=(-b+delta)/(2*a)
    r2=(-b-delta)/(2*a)
    print('As raízes dessa equação são',r1,'e',r2,'respectivamente.')

except:
    print('As raízes dessa equação não existem no conjunto de números reais')