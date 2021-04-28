codOperario=1
totalFolhaPg=0
totalPecasFabricadas=0
salarioMinimo=1045
mediaPecasMulherA=0
mediaPecasMulherB=0
mediaPecasMulherC=0
mediaPecasHomemA=0
mediaPecasHomemB=0
mediaPecasHomemC=0
totalPecasMulherA=0
totalPecasMulherB=0
totalPecasMulherC=0
totalPecasHomemA=0
totalPecasHomemB=0
totalPecasHomemC=0
maiorSalario=0
sexoOperario="a"

while codOperario !=0:s
    codOperario=input("Código do operário: ")
    while sexoOperario!="F" and sexoOperario!="M":
        sexoOperario=input("Sexo (F ou M): ").upper()
    numPecasFacricadas=int(input("Peças fabricadas no mês: "))

    if numPecasFacricadas<=30:
        salario=salarioMinimo
        if sexoOperario=="F":
            mediaPecasMulherA=mediaPecasMulherA+numPecasFacricadas
            totalPecasMulherA=totalPecasMulherA+1
        else:
            mediaPecasHomemA=mediaPecasHomemA+numPecasFacricadas
            totalPecasHomemA=totalPecasHomemA+1
    
    elif numPecasFacricadas>30 or numPecasFacricadas<=35:
        salario=(((numPecasFacricadas-30)*0.03)*salarioMinimo)+salarioMinimo
        if sexoOperario=="F":
            mediaPecasMulherB=mediaPecasMulherB+numPecasFacricadas
            totalPecasHomemB=totalPecasHomemB+1
        else:
            mediaPecasHomemB=mediaPecasHomemB+numPecasFacricadas
            totalPecasHomemB=totalPecasHomemB+1

    elif numPecasFacricadas>35:
        salario=(((numPecasFacricadas-30)*0.05)*salarioMinimo)+salarioMinimo
        if sexoOperario=="F":
            mediaPecasMulherC=mediaPecasMulherC+numPecasFacricadas
            totalPecasHomemC=totalPecasHomemC+1
        else:
            mediaPecasHomemC=mediaPecasHomemC+numPecasFacricadas
            totalPecasHomemC=totalPecasHomemC+1
   
    totalFolhaPg=totalFolhaPg+salario
    totalPecasFabricadas=totalPecasFabricadas+numPecasFacricadas

    if salario>maiorSalario:
        codOperarioMaiorSalario=codOperario
        maiorSalario=salario
    
    print("O salário do operário",codOperario,"é R${:.2f}".format(salario))
    sexoOperario="a"

mediaPecasHomemA=mediaPecasHomemA/totalPecasHomemA
mediaPecasHomemB=mediaPecasHomemB/totalPecasHomemB
mediaPecasHomemC=mediaPecasHomemC/totalPecasHomemC
mediaPecasMulherA=mediaPecasMulherA/totalPecasMulherA
mediaPecasMulherB=mediaPecasMulherB/totalPecasMulherB
mediaPecasMulherC=mediaPecasMulherC/totalPecasMulherC
    
print("O total da folha de pagamento mensal é R${:.2f}".format(totalFolhaPg))
print("O total de peças fabricadas no mês é",totalPecasFabricadas)
print("A média de peças fabricadas por Homens da classe A é: {:.1f}".format(mediaPecasHomemA))
print("A média de peças fabricadas por Homens da classe B é: {:.1f}".format(mediaPecasHomemA))
print("A média de peças fabricadas por Homens da classe C é: {:.1f}".format(mediaPecasHomemA))
print("A média de peças fabricadas por Mulheres da classe A é: {:.1f}".format(mediaPecasHomemA))
print("A média de peças fabricadas por Mulheres da classe B é: {:.1f}".format(mediaPecasHomemA))
print("A média de peças fabricadas por Mulheres da classe C é: {:.1f}".format(mediaPecasHomemA))
print("O operário com o maios salário mensal foi",codOperarioMaiorSalario)

            

