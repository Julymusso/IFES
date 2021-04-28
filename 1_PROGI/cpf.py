def validacao(cpf):
    original=cpf
    verificacao=False
    digito2=cpf%10
    cpf=cpf//10
    digito1=cpf%10
    cpf=cpf//10
    soma=0
    for i in range (2,11):
        cpfSeparado=cpf%10
        soma=soma+(cpfSeparado*i)
        cpf=cpf//10
    verificador1=soma%11
    if verificador1>2:
        verificador1=11-verificador1
    else:
        verificador1=0
    if verificador1==digito1:
        soma=0
        cpf=original
        cpf=cpf//10
        for j in range (2,12):
            cpfSeparado=cpf%10
            soma=soma+(cpfSeparado*i)
            cpf=cpf//10
        verificador2=soma%11
        print(verificador2)
        if verificador2>2:
            verificador2=11-verificador2
        else:
            verificador2=0
        if verificador2==digito2:
            verificacao=True
    return verificacao

#main
numero=int(input("Insira o número do CPF (apenas dígitos): "))
if validacao(numero)==True:
    print("O cpf",numero,"é válido")
else:
    print("O cpf",numero,"não é válido")
