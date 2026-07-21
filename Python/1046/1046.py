times    = input().split()
times    = [int(time) for time in times]
if(times[0] == times[1]):
    print("O JOGO DUROU 24 HORA(S)")
elif(times[0] > times[1]):
    print(f"O JOGO DUROU {(24-times[0])+times[1]} HORA(S)")
else:
    print(f"O JOGO DUROU {times[1] - times[0]} HORA(S)")