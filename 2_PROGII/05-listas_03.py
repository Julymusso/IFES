# (n+1)=(n)+(n-1) 
# caso termo <= 2, soma 1 + 1
# se não, soma n = n-1

def fibonacci (n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

numero = int(input("\nQual termo da sequencia Fibonacci gostaria de saber: "))
print ("\n {}".format(fibonacci(numero)))