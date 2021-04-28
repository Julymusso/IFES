# Ler quatro valores referentes a quatro notas escolares de um aluno e escrever uma mensagem dizendo
# que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o aluno não for aprovado
# indicar uma mensagem informando esta condição. Apresentar junto das mensagens o valor da média do
# aluno para qualquer condição. 

print('Este app cálcula a média de pontos de um aluno e informa a situação do mesmo (Aprovado ou Reprovado)')

nome=input('Digite o nome do aluno: ')

cont=0
soma=0

while cont < 4:
    nota=int(input('Digite a nota do aluno: '))
    soma=soma+nota

    cont=cont+1

media=soma/cont

if media >= 7:
    situacao='Aprovado'
else:
    situacao='Reprovado'

print(nome,'está',situacao,'com média final',media)