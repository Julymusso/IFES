def inverter (l,p1,p2):
    aux=l[p1]
    l[p1]=l[p2]
    l[p2]=aux

teste=[1,5,6,9,8,4,2,3,6,5,9,6,1,5,5]
inverter(teste,5,9)
print (teste)
