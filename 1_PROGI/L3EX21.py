

print('Este app calcula o IMC')

nome=input('Digite o nome: ')
altura=float(input('Digite a altura: '))
sexo=input('Digite o sexo (M ou F)').lower()

if sexo=='m':
    peso_ideal=72.7*altura-58
elif sexo=='f':
    peso_ideal=62.1*altura-44.7

print (nome+"\n"+"seu peso ideal e "+str(peso_ideal))