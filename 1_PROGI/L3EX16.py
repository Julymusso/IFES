# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá
# ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)

print('Este app informa se voce pode ou não votar esse ano')

ano_nascimento=int(input('Digite o ano de nascimento (AAAA): '))
ano_atual=int(input('Digite o ano atual (AAAA) '))

idade=ano_atual-ano_nascimento

if idade>=16:
    situacao="Apto a votar"
else:
    situacao="Inapto a votar"

print ("Voce esta "+situacao)