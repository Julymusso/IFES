import pickle
import os

def lerArquivo():      
    if os.path.isfile("Multas.bin"):
        with open ("Multas.bin","rb") as arquivo:
            conteudo = pickle.load(arquivo)
        return conteudo
    else:
        naturezas = {"Leve":3, "Media":4, "Grave":5, "Gravissima":7}
        return {'Motoristas':{},'Veiculos':{},'Infracoes':[],'Naturezas':naturezas}

def salvarArquivo(conteudo):      
    with open("Multas.bin","wb") as arquivo:
        pickle.dump(conteudo,arquivo)

def data():
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    return (dia,mes,ano)

def natureza():    
    menu = ''' Insira a Natureza da Infração:
                1) Leve
                2) Média
                3) Grave
                4) Gravíssima\n'''

    op = int(input(menu))    
    while op != 0 or op != 1:
        if op == 1:
            natureza = "Leve"
            break
        elif op == 2:
            natureza = "Media"
            break
        elif op == 3:
            natureza = "Grave"
            break
        elif op == 4:
            natureza = "Gravissima"
            break
        print ("Opção inválida!\n")
        op = int(input(menu))

    return natureza

def cadastrarMotorista(dicionarioDados):
    dadosMotorista=dicionarioDados['Motoristas']
    
    cnh = input("Insira a CNH: ")
    
    if cnh not in dadosMotorista:
            
        nome = input("Insira o nome do motorista: ")
        
        print("Data de Nascimento")
        nascimento = data()

        dados=(nome,nascimento)
        dadosMotorista.update({cnh:dados})
        print ("\nMotorista Cadastrado com sucesso!\n")
    else:
        print("\nEsse motorista já está cadastrado na base de dados.\n")
    
    return dadosMotorista

def cadastrarVeiculos(dicionarioDados):
    dadosVeiculos = dicionarioDados['Veiculos']
    
    placa = input("Insira a placa do veículo: ")
    
    if placa not in dadosVeiculos:
            
        cnh = input("Insira a cnh do dono do veículo: ")
        modelo = input("Insira o modelo do veículo: ")
        cor = input("Insira a cor do veículo: ")

        dados = (cnh,modelo,cor)
        dadosVeiculos.update({placa:dados})
        print ("\nVeículo Cadastrado com sucesso!\n")
    else:
        print("\nEsse veículo já está cadastrado na base de dados.\n")
    return dadosVeiculos

def alterarProprietario(dicionarioDados):
    dadosVeiculos = dicionarioDados['Veiculos']
    dadosMotorista = dicionarioDados['Motoristas']
   
    placa = input("Insira a placa do veículo: ")
    
    if placa in dadosVeiculos:
        cnh = input("Insira a cnh do dono do veículo: ")

        if cnh in dadosMotorista:
            dados = dadosVeiculos[placa]
            
            modelo = dados[1]
            cor  = dados[2]
            dados = (cnh,modelo,cor)

            dadosVeiculos.update({placa:dados})
            
            print("\nAlteração realizada com sucesso! \n")
        else:
            print("\nCNH não cadastrada. \n Antes de prosseguir com nova tentativa, favor voltar ao menu e selecionar a opção 1.")
    else:
            print("\nVeículo não cadastrado. \n Selecione a opção 2 no menu inical para realizar um novo cadastro.")    
    return dadosVeiculos

def cadastrarInfracao(dicionarioDados):
    dadosInfracoes = dicionarioDados['Infracoes']
    dadosVeiculos = dicionarioDados['Veiculos']
    
    placa = input("Insira a placa do veículo: ")
    if placa in dadosVeiculos:
        dataInfracao = data()
        naturezaInfracao = natureza()

        if dadosInfracoes != []:
            idInfracao = int(dadosInfracoes[-1][0])+1
        else:
            idInfracao = 1
        
        dadosInfracoes.append((idInfracao,dataInfracao,placa,naturezaInfracao))
        print ('Infração nº {} adicionada com sucesso'.format(idInfracao))
    
    else:
        print("\nVeículo não cadastrado. \n Selecione a opção 2 no menu inical para realizar um novo cadastro.")
    return dadosInfracoes

def main (Argv=None):
    menu = '''
    MENU

    Escolha uma opção:
        1) Cadastrar Motorista
        2) Cadastrar Veículos
        3) Alterar Proprietário
        4) Cadastrar Infração
        5) Sair\n'''

    print('SISTEMA DE MULTAS DE TRÂNSITO\n')

    dadosGerais = lerArquivo()

    op = int(input(menu))
    while op != 5:
        if op == 1:
            dadosGerais['Motoristas'] = cadastrarMotorista(dadosGerais)
            salvarArquivo(dadosGerais)
        elif op == 2:
            dadosGerais['Veiculos'] = cadastrarVeiculos(dadosGerais)
            salvarArquivo(dadosGerais)
        elif op == 3:
            dadosGerais['Veiculos'] = alterarProprietario(dadosGerais)
            salvarArquivo(dadosGerais)
        elif op == 4:
            dadosGerais['Infracoes'] = cadastrarInfracao(dadosGerais)
            salvarArquivo(dadosGerais)
        elif op != 5:
            print ('Opção inválida!\n Escolha uma das opções do Menu.\n Para sair do programa digite 5.\n')
        op = int(input(menu))

main()