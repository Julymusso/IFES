# Efetuar a leitura de três valores (variáveis A, B e C) e apresenta-los dispostos em ordem crescente. Para
# solucionar o problema, utilizar os conceitos da propriedade distributiva e troca de valores entre variáveis.

print('Este app coloca os números em ordem crescente')

a=float(input('Digite um número: '))
b=float(input('Digite um número: '))
c=float(input('Digite um número: '))


if a<b:
    ft=a
    if a<c:                         
        if b<c:
            sd=b
            th=c
        else:
            sd=c
            th=b

        
elif a>b:
    if b<c:
        print(b ,a ,c)

#a, b, c - ok
#a, c, b - ok
#b, a, c - 
#b, c, a
#c, a, b
#c, b, a
        
