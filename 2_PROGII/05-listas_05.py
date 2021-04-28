# x, y, z
# caso x > y, maior = x
# se não, maior = y


def maior_elemento (lista):
    for i in range(len(lista)):
        primeiro = i
        for j in range (i+1, len(lista)):
            if lista[primeiro] > lista[j]:
                return lista[primeiro]
            else:
                return maior_elemento(lista[1:])
jaca = [2,5,4,6,3,1,8,9,7,5,6,2]
print ("\n {}".format(maior_elemento(jaca)))