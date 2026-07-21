numbers = input().split()
numbers = [ float(number) for number in numbers ]
numbers = sorted(numbers, reverse=True)
A,B,C   = numbers[0],numbers[1],numbers[2]
if( A >= ( B + C ) ):
    print("NAO FORMA TRIANGULO")
else:
    if( (A**2) > ((B**2)+(C**2)) ):
        print("TRIANGULO OBTUSANGULO")
    elif( (A**2) < ((B**2)+(C**2)) ):
        print("TRIANGULO ACUTANGULO")
    else:
        print("TRIANGULO RETANGULO")
    
    if( A == B and B == C ):
        print("TRIANGULO EQUILATERO")
    elif( A == B or B == C or C == A ):
        print("TRIANGULO ISOSCELES")