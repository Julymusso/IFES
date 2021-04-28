def primos (k):
    for i in range (1,k+1):
        for j in range (1,i):
            if i%j==0:
                print()
            else:
                return j

print (primos(1024))
