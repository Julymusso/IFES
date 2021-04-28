def temperatura (n):
    temp=[]
    acima=0
    for i in range (0,n):
        temp.append(int(input("Qual é a temperatura do dia: ")))    
    media=sum(temp)/n
    for a in range (0,len(temp)):
        if temp[a]>media:
            acima=acima+1
    print ("Média: {:.1f} \n Dias acima da média: {:.0f}".format(media,acima))
    

temperatura(5)


