matricula = int(input("Digite sua matrícula: "))

A = matricula//100000
matricula = matricula%100000
A = 2000 + (A*10) + (matricula//10000)
matricula = matricula%10000

S = str(matricula//1000)

D = matricula%1000

print ("Seu ano de matrícula é:",A,"Seu semestre de matricula é:",S+"º", "Sua ordem de matrícula é:",D)