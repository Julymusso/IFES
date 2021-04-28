
custo = [10,20,30,52,14,32,36,25,45,69,84,54,25,36]
venda = [20,25,36,60,30,60,50,30,73,86,120,60,41,49]


def Lucro (custo, venda):
    menos20=0
    mais25=0.0

    for (custo,venda) in lista:
        if venda < 1.2*custo:
            menos20 += 1
        if venda > 1.25*custo:
            mais25 += 1
    print ("Menor que 20, {}".format(menos20))
    print ("Porcentagem maior que 25 {:.2f}%".format(mais25/len(custo)))

Lucro(lista)
