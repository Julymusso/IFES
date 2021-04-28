#var
    #a, resto4, resto100, resto400: int

a=int(input("Digite um ano: "))

resto4 = a%4
resto100 = a%100
resto400 = a%400

if resto4==0:
    if resto100==0:
        if resto400==0:
            print("Bissexto")
        else:
            print("Não é bissexto")
    else:
        print("Bissexto")
else:
    print("Não é bissexto")