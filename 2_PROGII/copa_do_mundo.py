def somapontos (matriz):
    soma=0
    for _, pontos in matriz:
        soma+=pontos
    return soma

classifica = [("Brasil",3),("Australia",3),("Croacia",3)]
nJogos = 3
print(3*nJogos-somapontos(classifica))