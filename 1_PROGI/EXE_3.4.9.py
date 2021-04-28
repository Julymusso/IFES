def produto (num1,num2):
    soma=0
    while num1>=1:
        impar=num1%2
        if impar==1:
            soma=soma+num2
        num1=num1//2
        num2=num2*2
    return soma

for i in range (1,11):
    a=int(input("Insira um número: "))
    b=int(input("Insira um número: "))
    print("Produto:",produto(a,b))