original=1
binario=0
while original!=0:
    number=int(input("Insira um número de no máximo 5 algarismos: "))
    original=number
    while number>0:
        mod=number%2
        number=number//2
        if original==((number*2)+mod):
            binario=str(mod)
        else:
            binario=str(mod)+binario
    print("Decimal:",original,"\nBinario:",binario)
    binario=0