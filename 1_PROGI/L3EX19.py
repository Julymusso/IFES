# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de
# 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte

print('Este app cálculo o tempo de jogo')

hora_inicio=int(input('Digite a hora de inicio (HH-24h): '))
hora_final=int(input('Digite a hora de termino (HH-24h): '))

if hora_inicio<hora_final:
    tempo_jogo=hora_final-hora_inicio
else:
    tempo_jogo=(24-hora_inicio)+hora_final


print ("O jogo durou "+str(tempo_jogo)+" horas")