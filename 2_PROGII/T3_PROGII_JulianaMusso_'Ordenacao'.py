import pickle

def leitura():
    arquivo_entrada = input("Insira o nome e extensão do arquivo de entrada. Ex.: arquivo.bin\n")
    conteudo = []
    with open (arquivo_entrada,"rb") as arq:
        while True:
            try:
                conteudo.append(pickle.load(arq))
            except EOFError:
                break
    return conteudo

def salvar(conteudo):
    with open("saidaJRM.txt","a") as arq: 
        arq.write(conteudo+"\n")

def soma(lista):
    nota_total = 0
    for i in range (1,len(lista)-1):
        nota_total = nota_total+lista[i]
    return nota_total

def nota_tabela(lista,dic):
    lista_dados = []
    for i in range (0,len(lista)):
        nota_total = soma(lista[i])
        lista_dados.append([lista[i][0],dic[lista[i][0]],lista[i][1],lista[i][2],lista[i][3],lista[i][4],nota_total,lista[i][5]])
    return lista_dados

def quick_sort(lista,pmenor,pmaior):
    if pmenor < pmaior:
        posicao = divisao(lista,pmenor,pmaior)
        quick_sort(lista,pmenor,posicao-1)
        quick_sort(lista,posicao+1,pmaior)

def divisao(lista,pmenor,pmaior):
    pivot = lista[pmenor]
    i = pmenor+1
    j = pmaior
    while i <= j:
        while i <= j and criterios(lista[i],pivot):
            i+=1
        while j >= i and not criterios(lista[j],pivot):
            j -=1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[pmenor], lista[j] = lista[j], lista[pmenor]
    return j

def criterios(a,b):
    if a[6] > b[6]: #Total da Nota, decrescente
        return True
    if a[6] < b[6]:
        return False
    if a[3] > b[3]: #Segunda nota decrescente
        return True
    if a[3] < b[3]:
        return False
    if a[7] < b[7]:#Tempo de execução crescente
        return True
    if a[7] > b[7]:
        return False       
    if a[1] <= b[1]:#Nomes crescente
        return True
    else:
        return False

def bonus(lista):
    condicional = True
    i=0
    while condicional == True:
        lista[i][6]=lista[i][6]+2
        i+=1
        if i > 5:
            condicional = False
        elif lista[i-1][6]==lista[i][6] and lista[i-1][3]==lista[i][3] and lista[i-1][7]==lista[i][7]:
            condicional = True
    return lista

def exibir(lista):    
    for i in range (0,len(lista)):
        print ("{} {}".format(lista[i][1],lista[i][6]))

def main(Argv=None):
    dados = leitura()
    dic_nomes = dados[0]
    lista_notas = dados[1]
    lista_notas_totais = nota_tabela(lista_notas,dic_nomes)
    quick_sort(lista_notas_totais,0,len(lista_notas_totais)-1)
    lista_notas_totais = bonus(lista_notas_totais)
    exibir(lista_notas_totais)
main()