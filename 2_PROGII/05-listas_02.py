# l[1]+soma(l:), se len(l) > 0
# soma, caso contrário

def soma (l):
    if len(l) == 1:
        return  l[0]
    else:
        return l[0] + soma(l[1:])
       
def main(argv=None):
    num = int(input("\nInsira o tamanho da lista: "))
    lista = []
    for i in range (0,num):
        x=int(input("\nInsira um valor para a lista: "))
        lista.append(x)
    
    print("Soma = {}".format(soma(lista)))

main()
