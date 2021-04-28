
def calcPi(N):
    S=0
    cont=0
    for i in range (1,N+1,2):
        cont=cont+1
        imparPar=cont%2
        if imparPar==1:
            S=S+(1/(i**3))
        else:
            S=S-(1/(i**3))
    pi=(32*S)**(1/3)
    return pi

#main
numTermos=int(input("Insira o número de termo: "))
for i in range (1,numTermos+1):
    print("Termo:",i,"......... Pi: {:.5f}".format(calcPi(i)))

