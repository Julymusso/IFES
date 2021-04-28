# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
# mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é
# aprovado). Escrever também a média calculada.

print('Este app cálcula a media final no aluno e informa se ele foi aprovado ou reprovado')

n1=float(input('Digite a nota da primera prova: '))
n2=float(input('Digite a nota da segunda prova: '))

media=round((n1+n2)/2,1)

if media>=6:
    situacao="Aprovado"
else:
    situacao="Reprovado"

print ("O aluno foi "+situacao+" com media de "+str(media).replace('.',','))