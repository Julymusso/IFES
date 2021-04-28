numAproximacao=20
limitNumber=10000
inverso=0

for i in range (1,limitNumber):
    #capicuas
    num=i
    while num>0:
        digito = num%10
        inverso = inverso*10+digito
        num=num-digito
        num=num/10
    if i==inverso:
        # quadrados perfeitos
        x=i/2
        for j in range (1,numAproximacao):
            x=((x*x)+i)/(2*x)
        if x%1==0:
            print(i)
    inverso=0
