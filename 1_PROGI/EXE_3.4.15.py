def calcE(N):
    e=1
    for i in range (1,N+1):
        a=1
        for j in range (1,i+1):
            a=a*j
        e=e+(1/a)
    return e
    
#main
i=1
while calcE(i)<2.71818182846:
    i=i+1
print("Termo......",i)