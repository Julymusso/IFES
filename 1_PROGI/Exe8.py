#var
    #menor, maior, n: int

i=0
alto=0
pesada=0
mediaidade=0
cont=0

while i != "N":
    sexo=0
    idade=0
    peso=0
    altura=0
    i=0
    nome=input("Insira o nome do aleta: ")
    while sexo != "F" and sexo != "M":
        sexo=input("Sexo (F ou M): ").upper()
    while idade>150 or idade<=0:
        idade=int(input("Idade: "))
    while peso<=0:
        peso=float(input("Peso(kg): "))
    while altura<=0 or altura>3:
        altura=float(input("Altura(m): "))
    if sexo=="M" and altura>alto:
        alto=altura
        alunoalto=nome
    if sexo=="F" and peso>pesada:
        pesada=peso
        alunapesada=nome
    mediaidade=mediaidade+idade
    cont=cont+1
    while i != "S" and i != "N":
        i=input("Deseja inserir outro atleta (S ou N):").upper()
mediaidade=mediaidade/cont
print("O aluno mais alto: ",alunoalto)
print("A aluna com maior peso:",alunapesada)
print("A média de idade dos atletas: {:.0f}".format(mediaidade))
