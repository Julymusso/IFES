def fatorial(n):
    nFatorial=n
    for i in range(1,n):
        nFatorial=nFatorial*(n-i)
    return nFatorial
    