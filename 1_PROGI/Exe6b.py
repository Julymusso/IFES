#var
    #n, somapos, medianeg, cont: int
    #i: str
a=0
for i in range(1,11,1):
    a=0
    for j in range(1,i+1,1):
        a = a + (j)*(10**(i-j))
    print(i,a)
        

#(1,1)
#(2,1 2)
#(3,1 2 3)
#(4,1 2 3 4)