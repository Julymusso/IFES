def media (n):
    i=0
    notas=[]
    soma=0
    aprovados=0
    while i<n:
        notas.append(int(input("Nota: ")))
        soma=soma+notas[i]
        if notas[i]>60:
            aprovados=aprovados+1
        i+=1
    media=soma/n
    print("Média da Turma: {:.1f} \n Número de aprovados: {:.f}".format(media,aprovados))

print(media(5))
