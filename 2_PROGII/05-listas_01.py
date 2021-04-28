# x.(x-1)!, se x > 0
# 1, caso contrário

def fatorial (n):
    if n <= 0:
        return 1
    else:
        return n*fatorial(n-1)
    
def main (argv=None):
    num = int(input("Insira um número para calcular o fatorial: "))
    print ("\n{}".format(fatorial(num)))

main()