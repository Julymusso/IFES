#var
    #n, somapos, medianeg, cont: int
    #i: str
i='s'
somapos=0
medianeg=0
cont=0
while i!='n':
    n=int(input('Digite um número: '))
    if n>0:
        somapos=somapos+n
    else:
        medianeg=medianeg+n
        cont=cont+1
    i=input("Desejar continuar (s) ou (n)? ")
medianeg=medianeg/cont
print ("Soma dos positivos:",somapos,"e Média dos negativos:",medianeg)

