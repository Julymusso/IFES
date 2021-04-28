
def determinante (M):
    d1=M[0][0]*M[1][1]*M[2][2]
    d2=M[0][1]*M[1][2]*M[2][0]
    d3=M[0][2]*M[1][0]*M[2][1]
    s1=d1+d2+d3

    d4=M[0][2]*M[1][1]*M[2][0]
    d5=M[0][0]*M[1][2]*M[2][1]
    d6=M[0][1]*M[1][0]*M[2][2]
    s2=d4+d5+d6

    return s1-s2

def alinhados(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3

    matriz=[[x1,y1,1],[x2,y2,1],[x3,y3,1]]

    return determinante(matriz)==0

ponto1=(2,1)
ponto2=(7,5)
ponto3=(9,6)
print(alinhados(ponto1,ponto2,ponto3))
