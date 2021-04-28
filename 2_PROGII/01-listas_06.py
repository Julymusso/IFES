def maximo (l):
    maior=l[0]
    i=1
    while i < len(l):
        if l[i]>maior:
            maior=l[i]
            posicao=i
        i += 1
    return posicao


teste=[1,5,6,9,8,4,2,3,6,5,9,6,1,5,5]
print(maximo(teste))
