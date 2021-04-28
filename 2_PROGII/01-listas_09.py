def ordenadas (l1,l2):
    i=0
    a=0
    b=0
    while i<len(l1):
        if l1[i]%2==0:
            a += 1
        if l2[i]%2!=0:
            b += 1
        i += 1
    if a>=b:
        i=0
        soma=0
        while i < (len(l1)-1):
            soma=l1[i]+soma
            i += 1
        print(soma)
    else:
        i=0
        prod=1
        while i < (len(l2)-1):
            prod=l2[i]*prod
            i += 1
        print(prod) 

listaa=[1,5,3,6,9,5,8,7]
listab=[1,5,3,6,9,5,8,7]
ordenadas(listaa,listab)
