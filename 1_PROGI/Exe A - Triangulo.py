#var
#L1, L2, L3: real
#início
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
if l1+l2>l3 and l1+l3>l2 and l3+l2>l1:
    if l1==l2 and l2==l3 and l3==l1:
        print("Equilátero")
    elif l1==l2 or l2==l3 or l3==l1:
        print("Isóceles")
    else:
        print ("Escaleno")
else:
    print ("Não é um triângulo")