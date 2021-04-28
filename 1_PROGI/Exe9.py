#var
    #cod: str
    #preco, maiorpreco, mediapreco: float
mediapreco=0
maiorpreco=0
for i in range (1,16,1):
    cod=input("Insira o código do produto: ")
    preco=float(input("Insira o valor do produto: "))
    mediapreco=mediapreco+preco
    if preco>maiorpreco:
        maiorpreco=preco
mediapreco=mediapreco/(i)
print("O Maior preço é:",maiorpreco)
print("Média de preços dos produto:",mediapreco)

