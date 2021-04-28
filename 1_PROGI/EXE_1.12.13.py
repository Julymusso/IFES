numConsumidor=1
entrada=True
mediaGeralConsumo=0
residencial=0
comercial=0
industrial=0
precoKwh = float(input("Informe o valor do kWh: "))
while numConsumidor != 0:
    if numConsumidor==0:
        pass
    else:
        numConsumidor=int(input("Digite o código do consumidor: "))
        tipoConsumidor=input("Digite qual o tipo de consumidor (R-Residencial/ C-Comercial/ I-Industrial): ")
        qtdKwhMensal=float(input("Digite o consumo em kWh: "))
        if entrada==True:
            maiorConsumo=qtdKwhMensal
            menorConsumo=qtdKwhMensal
            entrada=False
        if tipoConsumidor=="R":
            residencial=residencial+qtdKwhMensal
        elif tipoConsumidor=="C":
            comercial=comercial+qtdKwhMensal
        elif tipoConsumidor=="I":
            industrial=industrial+qtdKwhMensal
        mediaGeralConsumo=mediaGeralConsumo+qtdKwhMensal
        valorTotal=qtdKwhMensal*precoKwh
        print("Consumidor: ",numConsumidor,"\nValot Total: R${:.2f}".format(valorTotal))
totalConsumidores=residencial+comercial+industrial
mediaGeralConsumo=mediaGeralConsumo/totalConsumidores
print("Maior consumo: {:.1f}kWh".format(maiorConsumo))
print("Menor consumo: {:.1f}kWh".format(menorConsumo))
print("Consumo residencial: {:.1f}kWh".format(residencial))
print("Consumo comercial: {:.1f}kWh".format(comercial))
print("Consumo industrial: {:.1f}kWh".format(industrial))
print("Média Geral de Consumo: {:.1f}kWh".format(mediaGeralConsumo))


