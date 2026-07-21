string = input().split()
a,b,c  = float(string[0]),float(string[1]),float(string[2])
pi     = 3.14159
print(f"TRIANGULO: {((a*c)/2):.3f}\nCIRCULO: {(pi*(c**2)):.3f}\nTRAPEZIO: {(((a+b)*c)/2):.3f}\nQUADRADO: {(b**2):.3f}\nRETANGULO: {(a*b):.3f}")