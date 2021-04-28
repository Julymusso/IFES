import os

def limpatela():
    if os.name=="nt": #nome do windows
        os.system("cls") #limpar tela do windows
    else:
        os.system("clear") #limpar tela do linux

def visualizarjogadores(jogadores):
    if len(jogadores) == 0:
        print("Não existe jogadores cadastrados.")
    else:
        print("Jpgadores cadastrados no sistema: ")

    for nome, cpf in jogadores:
        print("{} (CPF: {})".format(nome,cpf))
    
    print("\n")

def existecpf(jogadores,ncpf):
    for _, cpf in jogadores:
        if cpf == ncpf:
            return True
    return False

def inserirjogador(jogadores):
    visualizarjogadores(jogadores)

    nome = input("Digite o nome do jogador: ")
    cpf = input("Digite o cpf do jogador: ")
    
    if existecpf(jogadores,cpf):
        print("Esse jogador já está cadastrado.\n")
    else:
        print ("Jogador Cadastrado com sucesso!\n")
        jogadores.append((nome,cpf))

def lercpfs(jogadores):
    n=int(input("Insira a quantidade de participantes: "))
    cpfs=[]

    while len(cpfs) < n:
        visualizarjogadores(jogadores)
        ncpf = input("Insira um CPF: ")
                
        while (ncpf in cpfs) or (not existecpf(jogadores,ncpf)):
            print("CPF inválido.\n")
            ncpf = input("Tente outro CPF: ")

        cpfs.append(ncpf)
    print("Jogadores cadastrados com sucesso!\n") 
    return cpfs

def lernumeros():
    n=int(input("Quantos números deseja jogar: "))
    while n < 6 or n > 15:
        print ("Erro: As apostas são compostas por no mínimo sei números e no máximo 15.\nTente novamente.\n")
        n=int(input("Quantos números deseja jogar: "))
    
    numeros=[]
    while len(numeros)<n:
        x = int(input("Digite um número: "))

        while x < 1 or x > 60 or x in numeros:
            print("Erro: Digite um número entre 1 e 60. Não pode utilizar números repetidos.\nTente novamente.\n")
            x = int(input("Digite um número: "))
        
        numeros.append(x)
    return numeros

def cadastrarapostas(jogadores,apostas):
    cpfs = lercpfs(jogadores)
    numeros = lernumeros()

    apostas.append((cpfs,numeros))
    print("Aposta cadastrada com sucesso!\n")

def nomejogador(jogadores,cpf):
    for n, c in jogadores:
        if c==cpf:
            return n

def visualizarapostas(jogadores,apostas):
    i = 0
    while i < len(apostas):
        cpfs, numeros = apostas[i]

        print ("APOSTA {}".format(i+1))
        print("Números:",end=" ")
        
        for n in numeros:
            print(n, end = " ")
        print()
        print("Jogadores: ")
        
        for cpf in cpfs:
            print(nomejogador(jogadores,cpf))
    
        print ("")
        i+=1

def lernumerossorteados():
    l = []
    i=1
    while len(l) < 6:
        x = int(input("Digite o {}º número sorteado: ".format(i)))
        if x < 0 or x > 60 or x in l:
            print("Erro: Número inválido.\n")
        else:
            l.append(x)
            i+=1
    return l

def contida (lsorteados, lapostas):
    for x in lsorteados:
        if x not in lapostas:
            return False
    return True

def verificarapostasvencedoras(apostas,numeros):
    l=[]
    for i in range(len(apostas)):
        _,nums = apostas[i]

        if contida(numeros,nums):
            l.append(i)
    return l

def listavencedores(jogadores,apostas,vencedores,premioporcartao):
    limpatela()
    print("Vencedores: ")
    
    for i in vencedores:
        cpfs,_ = apostas[i]

        print("CARTÃO {}".format(i+1))

    for ncpf in cpfs:
        print("{} - R$ {:.2f}.format(nomejogador(jogadores,ncpf),premioporcartao/len(cpfs))")


def cadastrarsorteio (jogadores, apostas):
    numeros = lernumerossorteados()
    vencedores = verificarapostasvencedoras(apostas,numeros)

    premio = int(input("Digite o valor total do prêmio: "))
    if len(vencedores) > 0:
        premioporcartao = premio/len(vencedores)
        listavencedores(jogadores,apostas,vencedores,premioporcartao)
    else:
        print("Não houve vencedores. Prêmio acumulado.")

def main(argv=None):
    
    print("Seja Bem Vindo ao Bolão")
    menu = '''
    Escolha uma opção:

        1)Cadastrar Jogador
        2)Visualizar Jogador
        3)Cadastrar Aposta
        4)Visualizar Apostas
        5)Inserir Sorteio e listar vencedores
        6)Sair
    '''
    jogadores=[]
    apostas=[]    

    opcao = int(input(menu))
    while opcao != 6:
        if opcao == 1:
            inserirjogador(jogadores)

        elif opcao == 2:
            visualizarjogadores(jogadores)

        elif opcao == 3:
            cadastrarapostas(jogadores,apostas)

        elif opcao == 4:
            visualizarapostas(jogadores,apostas)
            
        elif opcao == 5:
            cadastrarsorteio(jogadores, apostas)

        elif opcao != 6:
            print ("Opção inválida! Tente novamente.\n")
        opcao = int(input(menu))

limpatela()
main()

#with open("nome_do_arquivo","w") as f:

    #f.wirte("teste salva")
    #pickle.dump(variavel,f)
# w (write): escrever no arquivo. sobrescreve
# r (read): ler arquivo
# a (append): adicionar ao arquivo. adiciona
# r+ (read/write): ler e escrever. não aconselho usar



