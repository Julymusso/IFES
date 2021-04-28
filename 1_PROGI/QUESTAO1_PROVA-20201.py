#JULIANA RICATO MUSSO SILVA
#20201BSI0230

def f_quadrado (n):
    quadrado=n**2
    return quadrado

def f_fatorial (n):
    fatorial=1
    for i in range (1,n+1):
        fatorial=fatorial*i
    return fatorial

#main
baseDivisor=0
S=0
termo=0
nTermos=7
for i in range (nTermos,0,-1):
    baseDividendo=i*10
    baseDivisor=baseDivisor+1
    termo=f_quadrado(baseDividendo)/f_fatorial(baseDivisor)
    if baseDivisor%2==1:
        S=S+termo
    else:
        S=S-termo
print ("{:.1f}".format(S))