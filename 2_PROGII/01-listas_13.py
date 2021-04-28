def iguais (l1,l2):
    same=0
    for i in range (len(l1)):
        if l1[i]==l2[i]:
            same += 1
    return same


testea=[1,5,6,3,2,4,8,9,6,5,3,7,5,6,4,8,3,2,5,6,4,5,4,8,9,9]
testeb=[5,4,6,9,8,7,5,5,3,2,1,4,6,5,7,8,9,6,3,2,1,4,5,6,9,8]
print(iguais(testea,testeb))
    
