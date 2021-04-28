audiencia4=0
audiencia5=0
audiencia7=0
audiencia12=0
num_canal="1"

while num_canal != "0":
    while num_canal != "0" and num_canal != "4" and num_canal != "5" and num_canal != "7" and num_canal != "12":
        num_canal=input("Digite o número do canal assistido nessa residência.\n")
        if num_canal != "0" and num_canal != "4" and num_canal != "5" and num_canal != "7" and num_canal != "12":
            print("Canal inválido")
        elif num_canal == "0":
            pass
        else:    
            qtd_expectadores=int(input("Digite o número de expectadores nessa residência.\n")) 
            if num_canal=="4":
                audiencia4=audiencia4+qtd_expectadores
            elif num_canal=="5":
                audiencia5=audiencia5+qtd_expectadores
            elif num_canal=="7":
                audiencia7=audiencia7+qtd_expectadores
            elif num_canal=="12":
                audiencia12=audiencia12+qtd_expectadores
            num_canal="1"

total=audiencia4+audiencia5+audiencia7+audiencia12
if total == 0:
    print("Não foram inseridos dados suficientes para o cálculo da audiência")
else:
    audiencia4=audiencia4/total
    audiencia5=audiencia5/total
    audiencia7=audiencia7/total
    audiencia12=audiencia12/total
    print("A audiência do Canal 4 foi de: {:.2f}%\n".format(audiencia4*100))
    print("A audiência do Canal 5 foi de: {:.2f}%\n".format(audiencia5*100))
    print("A audiência do Canal 7 foi de: {:.2f}%\n".format(audiencia7*100))
    print("A audiência do Canal 12 foi de: {:.2f}%\n".format(audiencia12*100))