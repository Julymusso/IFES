#var
    #a,b,c,d,r1,r2: float

a=float(input("Digite um número: "))

if a==0:
    print("Não é uma equação do segundo grau")
else:
    d=b*b-4*a*c
    if d<0:
        print("Não existe raízes reais")
    else:
        r1=(-b+d**(1/2)/(2*a))
        r2=(-b-d**(1/2)/(2*a))
        print (r1,"\n",r2)