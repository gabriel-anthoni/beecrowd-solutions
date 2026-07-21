times    = input().split()
times    = [int(time) for time in times]

if(times[0] == times[2] and times[1] >= times[3]):
    hours = 23
elif(times[0] > times[2]):
    hours = (24-times[0])+times[2]
else:
    hours = times[2]-times[0]

if(times[1] == times[3]):
    minutes = 0
    if(hours == 23):
        hours += 1
elif(times[1] > times[3]):
    minutes = (60-times[1])+times[3]
    if(times[0] != times[2]):
        hours -= 1
else:
    minutes = times[3]-times[1]

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")