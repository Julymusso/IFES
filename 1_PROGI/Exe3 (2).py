#var
    #n, pos, neg: int
    #i: str
i='s'
pos=0
neg=0
while i!='n':
    n=int(input('Digite um número: '))
    if n>0:
        pos=pos+n
    else:
        neg=neg+n
    i=input("Desejar continuar (s) ou (n)? ")
print ("Positivos:",pos,"e Negativos:",neg)

