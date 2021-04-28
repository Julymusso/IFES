# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40
# horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um
# algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do
# funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês
# possua 4 semanas exatas)

print('Este app cálculo salário total do funcionario')

horas_trabalhadas=int(input('Digite a quantidade horas trabalhadas no mes: '))
valor_hora=int(input('Digite o valor recebido por hora: '))

horas_extras=0

if horas_trabalhadas>160:
    horas_extras=horas_trabalhadas-160
    horas_trabalhadas=horas_trabalhadas-horas_extras
salario=round((horas_trabalhadas*valor_hora)+(valor_hora*0.5*horas_extras),2)

print ("O salaria mensal e R$"+str(salario).replace(".",","))