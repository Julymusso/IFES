def sublista (l,x,y):
    l2=[]
    for i in range (len(l)):
        if l[i]>x and l[i]<y:
            l2.append(l[i])
    return l2

lista=[6,5060,50,64,856,987,235,145,369,25,68,987,54,12,9856,3256,54,6,65,2,80,6325,]
print(sublista (lista,60,500))