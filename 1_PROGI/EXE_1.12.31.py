a=1
pi=0
cont=0
while 4/a>=0.0001:
    if cont%2==0:
        pi=pi+(4/a)
    else:
        pi=pi-(4/a)
    a=a+2
    cont=cont+1
print("Pi:",pi)