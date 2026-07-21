numbers = input().split()
a,b,c   = float(numbers[0]),float(numbers[1]),float(numbers[2])
delta   = ((b**2) - (4*a*c))
if ( a == 0 ) or ( delta < 0 ):
    print("Impossivel calcular")
else:
    print(f"R1 = {((-b + pow(delta,0.5))/(2*a)):.5f}\nR2 = {((-b - pow(delta,0.5))/(2*a)):.5f}")