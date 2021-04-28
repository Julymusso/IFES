""" codigo = int(input("Digite um número de 5 algarismos: "))

dezena_milhar = codigo // 10000
unidade = codigo % 10000
unidade_milhar = unidade // 1000
unidade = unidade % 1000
centena = unidade // 100
unidade = unidade % 100
dezena = unidade // 10
unidade = unidade % 10

soma = dezena_milhar*6 + unidade_milhar*5 + centena*4 + dezena*3 + unidade*2
digitoV = soma % 7

print("O dígito verificador é", digitoV) """


codigo = int(input("Digite um número de 5 algarismos: "))

i=10000
isoma=6
soma=0

while i != 1:
    dig = codigo // i
    codigo = codigo % i

    i = i/10
    soma = soma+(dig*isoma)
    isoma = isoma - 1
    print("Dígitos:",dig,"Código:",codigo,"incremento:",i,"incremento da soma:",isoma,"Soma:",soma)
digitoV = soma % 7
print("O dígito verificador é", digitoV)