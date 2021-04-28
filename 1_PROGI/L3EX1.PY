#Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor

print('Este app cálcula a diferença entre dois números inteiros\n')
n1=int(input('Digite um número: \n'))
n2=int(input('Digite um número: \n'))

if n1>n2:
    diferenca=n1-n2
    print('A diferença entre',n1,'e',n2,'é de',diferenca)
else:
    diferenca=n2-n1
    print('A diferença entre',n2,'e',n1,'é de',diferenca)
