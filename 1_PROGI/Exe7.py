#var
    #menor, maior, n: int
   
for i in range(0,100,1):
    n=int(input("Digite um número: "))
    if i==0:
        maior=n
        menor=n
    if n>maior:
        maior=n
    elif n<menor:
        menor=n
print("Menor:",menor," e Maior:",maior)    