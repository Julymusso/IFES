# Elaborar um programa que efetue a leitura de um valor que esteja entre a faixa de 1 a 9. Após a leitura
# do valor fornecido pelo usuário, o programa deverá indicar uma de duas mensagens: “O valor está na faixa
# permitida”, caso o usuário forneça o valor nesta faixa, ou a mensagem “O valor está fora da faixa permitida”,
# caso o usuário forneça valores menores que 1 ou maiores que 9

print('Este app indetifica numeros fora da faixa permitida')

a=float(input('Digite um numero maior que 1 e menor do que 9: '))

if a>1 and a<9:
    print ('Este numero esta dentro da faixa')
else:
    print ('Este numero esta fora da faixa')