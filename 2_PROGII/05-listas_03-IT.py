# (n+1)=(n)+(n-1) 
# caso termo <= 2, soma 1 + 1
# se não, soma n = n-1

def fibonacci (n):
    listaFib = []
    for i in range (0,n):
        if i < 2:
            listaFib.append(1)
        else:
            listaFib.append(listaFib[i-2] + listaFib[i-1])
    return listaFib[i]

numero = int(input("\nQual termo da sequencia Fibonacci gostaria de saber: "))
print ("\n {}".format(fibonacci(numero)))