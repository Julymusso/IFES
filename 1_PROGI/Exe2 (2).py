#var
    #n, media, cont: int
    #i: str
i='s'
cont=0
media=0
while i!='n':
    n=int(input('Digite um número: '))
    media=media+n
    cont=cont+1
    i=input("Desejar continuar somando (s) ou deseja encerrar o programa (n)? ")
media=media/cont
print (media)

