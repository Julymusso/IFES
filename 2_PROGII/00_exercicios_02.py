def fatorial(n):
    nFatorial=n
    for i in range(1,n):
        nFatorial=nFatorial*(n-i)
    return nFatorial
    
def combinacao(n,p):
    nCombin = fatorial(n)/(fatorial(p)*fatorial(n-p))
    return nCombin