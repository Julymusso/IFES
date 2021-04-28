def timeAlarm (hn,mn,ha,ma):
    hourNow=(hn*60)+mn
    hourAlarm=(ha*60)+ma
    timeSleep=hourAlarm-hourNow
    return timeSleep


hourNow=int(input("Hora atual: "))
minNow=int(input("Minutos atual: "))
hourAlarm=int(input("Hora alarme: "))
minAlarm=int(input("Minutos alarme: "))

print(timeAlarm(hourNow,minNow,hourAlarm,minAlarm),"minutos")
