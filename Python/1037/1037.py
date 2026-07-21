Range = float(input())
if   ( ( Range >= 0 ) and ( Range <= 25 )  ):
    print("Intervalo [0,25]")
elif ( ( Range > 25 ) and ( Range <= 50 )  ):
    print("Intervalo (25,50]")
elif ( ( Range > 50 ) and ( Range <= 75 )  ):
    print("Intervalo (50,75]")
elif ( ( Range > 75 ) and ( Range <= 100 ) ):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")