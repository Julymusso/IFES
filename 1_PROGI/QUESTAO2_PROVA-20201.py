#JULIANA RICATO MUSSO SILA
#20201BSI0230

def notaMedia (n1,n2,n3):
    nota=(n1+n2+n3)/3
    return nota

#main
nMediaAlunoMaior=0
nMediaAlunoMenor=0
nMediaTurma=0
nAlunosAprovados=0
nAlunosReprovadosPorFalta=0
nTotalAlunos=1
nMatricula="1"
nAlunoMediaMaior=0
nAlunoMediaMenor=0
flag=False

while nMatricula !="0":
    nMatricula=input("Digite a matrícula do aluno: ")
    if nMatricula != "0":
        nota1=float(input("Insira a primeira nota do aluno: "))
        nota2=float(input("Insira a segunda nota do aluno: "))
        nota3=float(input("Insira a terceira nota do aluno: "))
        nFrequencia=int(input("Insira a frequência do aluno: "))
        
        nMediaAluno=notaMedia(nota1,nota2,nota3)
        if nFrequencia>=40:
            if nMediaAluno>=60:
                situacaoAluno="Aprovado"
                nAlunosAprovados=nAlunosAprovados+1
            else:
                situacaoAluno="Reprovado"
        else:
            situacaoAluno="Reprovado"
            nAlunosReprovadosPorFalta=nAlunosReprovadosPorFalta+1

        if flag==False:
            nMediaAlunoMaior=nMediaAluno
            nMediaAlunoMenor=nMediaAluno
            nAlunoMediaMaior=nMatricula
            nAlunoMediaMenor=nMatricula
            flag=True

        if nMediaAluno>nMediaAlunoMaior:
            nMediaAlunoMaior=nMediaAluno
            nAlunoMediaMaior=nMatricula

        if nMediaAluno<nMediaAlunoMenor:
            nMediaAlunoMenor=nMediaAluno
            nAlunoMediaMenor=nMatricula
        
        nMediaTurma=nMediaTurma+nMediaAluno
        nTotalAlunos=nTotalAlunos+1

        print("Aluno:",nMatricula,"... Frequência:",nFrequencia,"... Nota Final: {:.1f}".format(nMediaAluno),"... Situação:",situacaoAluno)

print("Maior Media da Turma",".. Matricula:",nAlunoMediaMaior,"... {:.1f}".format(nMediaAlunoMaior))
print("Menor Media da Turma",".. Matricula:",nAlunoMediaMenor,"... {:.1f}".format(nMediaAlunoMenor))
print("Media da Turma: {:.1f}".format(nMediaTurma/(nTotalAlunos-1)))
print("Total de Aprovados:",nAlunosAprovados)
print("Alunos reprovados por falta: {:.0f}%".format(nAlunosReprovadosPorFalta/(nTotalAlunos-1)*100))
