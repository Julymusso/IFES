# Ler quatro valores referentes a quatro notas escolares de um aluno e escrever uma mensagem dizendo
# que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor
# do que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. Se a nova média for
# maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não
# foi aprovado, indicar uma mensagem informando esta condição. Apresentar com as mensagens o valor da
# média do aluno, para qualquer condição

print('Este app cálcula a média de pontos de um aluno, incluindo a prova final e informa a situação do mesmo (Aprovado ou Reprovado)')

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
    notaExame=int(input('Digite a nota da prova final: '))
    media=(media+notaExame)/2
    if media >= 5:
        situacao='Aprovado com prova final'
    else:    
        situacao='Reprovado'

print(nome,'está',situacao,'com média',media)