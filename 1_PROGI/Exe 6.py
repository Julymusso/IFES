#var
    #num, pos, neg, contmedia i: inteiro

pos=0
neg=0
contmedia=0

for i in range (0,20,1):
    num=int(input("Digite um número: "))
    if num>0:
        pos=pos+num
    else:
        neg=neg+num
        contmedia=contmedia+1
neg=neg/contmedia
print(pos,neg)
    
