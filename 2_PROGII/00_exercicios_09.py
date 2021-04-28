def xadrez (x,y,m,n):
    if x==m or y==n:
        return 1
    elif abs(x-m) == abs(y-n):
        return 1
    else:
        return 2

x1=0
x2=0
y1=0
y2=0
while x1<1 or x1>8:
    x1=int(input("Insira a coordenada X da primeira casa: "))
while y1<1 or y1>8:
    y1=int(input("Insira a coordenada Y da primeira casa: "))
while x2<1 or x2>8:
    x2=int(input("Insira a coordenada X da segunda casa: "))
while y2<1 or y2>8:
    y2=int(input("Insira a coordenada Y da segunda casa: "))
 
print (xadrez(x1,y1,x2,y2))
