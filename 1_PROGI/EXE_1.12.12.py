numAlunos = 7
notaMediaTurma=0
reprovadosFrequencia=0
reprovadosNota=0
entrada=True

for i in range (0,numAlunos+1,1):
    matricula = input("Digite a matricula do aluno: ")
    frequencia = int(input("Digite o número de aulas frequentadas pelo aluno: "))
    nota1 = int(input("Digite a primeira nota do aluno: "))
    nota2 = int(input("Digite a segunda nota do aluno: "))
    nota3 = int(input("Digite a terceira nota do aluno: "))    
    notaMedia = (nota1+nota2+nota3)/3
    if entrada == True:
        notaMaior=notaMedia
        notaMenor=notaMedia
        entrada=False
    if notaMedia > notaMaior:
        notaMaior=notaMedia
    elif notaMedia < notaMenor:
        notaMenor=notaMedia
    notaMediaTurma=notaMediaTurma+notaMedia
    if frequencia >= 40 and notaMedia >=60:
        situacao = "Aprovado"
    elif frequencia < 40:
        situacao="Reprovado"
        reprovadosFrequencia=reprovadosFrequencia+1
    elif notaMedia < 60:
        situacao="Reprovado"
        reprovadosNota=reprovadosNota+1
    print("O aluno:",matricula,"obteve a nota final {:.1f}".format(notaMedia),"e foi",situacao)
totalReprovados=reprovadosNota+reprovadosFrequencia
notaMediaTurma=notaMediaTurma/numAlunos
reprovadosFrequencia=reprovadosFrequencia/totalReprovados*100   
print("A Maior Média foi {:.1f}".format(notaMaior))
print("A Menor Média foi {:.1f}".format(notaMenor))
print("A nota média da turma é {:.1f}".format(notaMediaTurma))
print("O total de aluno reprovados foi",totalReprovados,"sendo que {:.0f}%".format(reprovadosFrequencia),"foram reprovados por infrequência")