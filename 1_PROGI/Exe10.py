salario=0
maiorsalario=0
mediasalario=0
mediafilhos=0
percentual=0
cont=0
while salario>=0:
    print("Casa",int(cont)+1)
    salario=float(input("Valor da renda:"))
    filhos=int(input("Número de filhos:"))
    mediasalario=mediasalario+salario
    mediafilhos=mediafilhos+filhos
    if salario>maiorsalario:
        maiorsalario=salario
    if salario<150:
        percentual=percentual+1
    cont=cont+1
mediasalario=(mediasalario-salario)/cont
mediafilhos=(mediafilhos-filhos)/cont
percentual=(percentual-1)/cont*100
print("Média Salarial: R${:.2f}".format(mediasalario))
print("Média do número de filhos: {:.0f}".format(mediafilhos))
print("Maior salário: R${:.2f}".format(maiorsalario))
print("Percentual de pessoas com salário menor que R$150,00: {:.2f}%".format(percentual))    