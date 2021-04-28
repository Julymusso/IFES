# x.x.x.x....x 
# caso termo <= 2, soma 1 + 1
# se não, soma n = n-1

def elevado (x,n):
    if n == 1:
        return x
    else:
        return x*elevado(x,n-1)

print ("\n {}".format(elevado(2,10)))