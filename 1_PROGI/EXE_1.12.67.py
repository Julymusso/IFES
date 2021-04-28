for i in range (5000,7000):
    primo=0
    for j in range (2,i):
        if i%j==0:
            primo=1      
    if primo==0:
        print("O numero:",i,"é primo")
    