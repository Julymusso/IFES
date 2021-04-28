import os

def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cadastrarNovoContato(contato):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    
    if verificarTelefone(contato,telefone) == False:
        contato.append((nome,telefone))
        print("Contato cadastrado com sucesso!") 
    
    else:
        print ("Erro: Esse telefone já está cadastrado.")
    
    return contato

def visualizarContato(contato):
    print("Contatos Cadastrados\n")
    for nome,telefone in contato:
        print("Nome: {} --- Telefone: {}".format(nome, telefone))

def verificarTelefone(contato,telefone):
    for _,tel in contato:
        if tel == telefone:
            return True
            break
        else:
            return False

def salvar(contato):
    arquivo = open("Contatos.txt","w")
    arquivo.write(str(len(contato))+"\n")
    
    for nome, telefone in contato:
        arquivo.write("{},{}\n".format(nome,telefone))
    arquivo.close()

def ler():
    if os.path.isfile("Contatos.txt"):
        arquivo = open("Contatos.txt","r")

        n = int(arquivo.readline()) #Lê primeira linha do arquivo
        contato = []

        for _ in range(n): #Lê o arquivo linha a linha
            linha = arquivo.readline() #Lê linha da lista (como é uma lista dentro de outra)
            lista = linha.split(",") # Lê a lista procurando a divisão por vírgula
            contato.append((lista[0],lista[1]))
        arquivo.close()
        return contato
    else:
        return []
        
def main(argv=None):
    print("Agenda de Contatos\n\n")
    
    menu = '''
Escolha uma opção:
    1) Cadastrar Contatos
    2) Visualizar Contatos
    3) Sair
'''

    op = int(input(menu))
    contatos = ler()
    while op != 3:
        limpaTela()
        if op == 1:
            cadastrarNovoContato(contatos)
            salvar(contatos)
        elif op == 2:
            visualizarContato(contatos)
        elif op != 3:
            print("Opção inválida. Tente novamente.\n")
        op = int(input(menu))

main()    