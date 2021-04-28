#var
    #D,M,A,Resto: int

D=0
M=0
A=0
Resto=0

D=int(input("Digite um número: "))
M=int(input("Digite um número: "))
A=int(input("Digite um número: "))

if M==2:
    Resto=A%4
    if Resto==0:
        if D>0 and D<30:
            print("Válida")
        else:
            print("Inválida")
    elif D>0 and D<29:
         print("Válida")
    else:
        print("Inválida")
elif M==4 or M==6 or M==9 or M==11:
    if D>0 and D<31:
        print("Válida")
    else:
        print("Inválida")
elif D>0 and D<32:
    print("Válida")
else:
    print("Inválida")
