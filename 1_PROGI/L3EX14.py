# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
# pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total
# da compra

print('Este app cálcula o valor da compra de MAÇÃS')

a=int(input('Digite a quantidade de maçãs que deseja adquirir: '))

if a>0 and a<12:
    total = a*1.3
elif a>0 and a>=12:
    total = a*1

print ('O valor total para esta compra é de:',total)