def numPrimo(numero):
    flag=True
    for i in range (2,numero):
        resto=numero%i
        if resto==0:
            flag=False
    return flag

#main
num=2
while num>0:
    num=int(input("Insira um número par maior que 2: "))
    if num>0 and num%2==0:
        primo1=0
        primo2=0
        original=num
        num=int(num/2)
        if num%2==1:
            incr=0
        else:
            incr=1
        while primo1+primo2!=original:
            i=num-incr
            if numPrimo(i)==True:    
                primo1=i
            i=num+incr
            if numPrimo(i)==True:
                primo2=i
            incr=incr+1
        print(original,"=",primo1,"+",primo2)
