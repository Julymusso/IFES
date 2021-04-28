
n1=480
n2=10
soma=0
for i in range (0,30,1):    
    div=n1/n2
    if i%2==0:
        soma=soma+div
    else:
        soma=soma-div
    n1=n1-5
    n2=n2+1
print(soma)
