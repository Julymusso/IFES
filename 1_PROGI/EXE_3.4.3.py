def soma(a,b,c,d):
    if a<b:
        if c<d:
            if a<c:
                menor=a
            else:
                menor=c 
        elif a<d:
            menor=a
        else:
            menor=d
    elif b<c:
        menor=b
    else:
        menor=c
    if menor==a:
        return (b+c+d)
    elif menor==b:
        return (a+c+d)
    elif menor==c:
        return(a+b+d)
    else:
        return(a+b+c)

for i in range (1,81):
    matricula=input("Insira a matrícula do aluno: ")
    n1=int(input("Insira a primeira nota: "))
    n2=int(input("Insira a segunda nota: "))
    n3=int(input("Insira a terceira nota: "))
    n4=int(input("Insira a quarta nota: "))
    npf=int(input("Insira a nota da prova final:"))

    notaFinal=(soma(n1,n2,n3,n4)+npf)

    if notaFinal>=0 and notaFinal<40:
        conceito="F"
    elif notaFinal>=40 and notaFinal<60:
        conceito="E"
    elif notaFinal>=60 and notaFinal<70:
        conceito="D"
    elif notaFinal>=70 and notaFinal<80:
        conceito="C"
    elif notaFinal>=80 and notaFinal<90:
        conceito="B"
    elif notaFinal>=90 and notaFinal<=100:
        conceito="A"

    print("Aluno:",matricula,"\nNota Final:",notaFinal,"\nConceito:",conceito)
