from random import randint
import os
import pickle

def limpatela():
    if os.name=="nt": #nome do windows
        os.system("cls") #limpar tela do windows
    else:
        os.system("clear") #limpar tela do linux


def salvarArquivo(recordista):      
    with open("Genius_Recorde.bin","wb") as arquivo:
        pickle.dump(recordista,arquivo)


def lerArquivo():      
    if os.path.isfile("Genius_Recorde.bin"):
        with open ("Genius_Recorde.bin","rb") as arquivo:
            x = (pickle.load(arquivo))

        return x
    else:
        return ["",0]

def compareLista(l1,l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
        i=+1
    return True

def stringToInterger (string):
    lista =[]
    for i in range(len(string)):
        lista.append(int(string[i]))
        i=+1
    return lista

def maiorRecorde(pontuacaoAtual,recordeGeral,nome):
    if pontuacaoAtual > recordeGeral:
        recordeGeral = pontuacaoAtual
        nome = input("Parabéns! Você é o novo recordista desse jogo.\nDigite Seu nome: ")
    recordista = (nome,recordeGeral)
    return recordista

            
def jogo():
    
    sorteado = randint(0,9)
    correta = []
    correta.append(sorteado)
   
    print("O primeiro numero sorteado foi: {}".format(sorteado))

    tentativa =[]
    tentativa.append(int(input("Digite a sequencia completa: ")))

    while compareLista(correta,tentativa) == True:
        print(compareLista(correta,tentativa))###
        sorteado = randint(0,9)
        correta.append(sorteado)
        limpatela()
        print("O novo número é:",sorteado)
        tentativa = stringToInterger(input("Digite a sequencia completa:"))

    pontuacao = len(correta)-1
    print ("Errou!\nVocê acertou um total de {} números\n\n".format(pontuacao))
    
    return pontuacao


def main(argv=None): 
    menu = '''    
    MENU

    Escolha uma opção:
    1) Iniciar novo jogo
    2) Sair
    '''
    print ("Seja bem vindo ao GENIUS\nVamos ver se você realmente tem boa memória.\nDesafie-se e desafie seu amigos.\n")
    recordeParcial = 0

    op = int(input(menu))
    while op != 2:
        if op == 1:
            x = lerArquivo()
            nome = x[0]
            recordeGeral = x[1]
            print("\nO recorde desse jogo é de {} com {} acertos seguidos.\n".format(nome,recordeGeral))
            print("O recorde dessa rodada é de : {} acertos seguidos.\n".format(recordeParcial))
            pontuacaoAtual = jogo()
            recordista = maiorRecorde(pontuacaoAtual,recordeGeral,nome)
            salvarArquivo(recordista)
            if pontuacaoAtual > recordeParcial:
                recordeParcial = pontuacaoAtual 
        elif op != 2:
            print("Opção inválida!\nTente novamente.")
        op = int(input(menu))
    
main()