#delta = b²-4ac
#-b+-delta/2a
#var
#A, B, C, X1, X2, delta: float
#início
A=float(input("Insira A, multiplicador do X²: "))
B=float(input("Insira B, multiplicador do X: "))
C=float(input("Insira C, contante: "))

delta = ((B**2)-(4*A*C))**(1/2)
X1 = -(delta+B)/(2*A)
X2 = (delta-B)/(2*A)
print ("As raízes da equação são X1:{:.2f} e X2:{:.2f}".format(X1, X2))