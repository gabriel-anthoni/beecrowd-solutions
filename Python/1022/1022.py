import math

n = int(input())

for _ in range(n):

    entrada = input().split()
    
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    op = entrada[3]
    n2 = int(entrada[4])
    d2 = int(entrada[6])
    
    if op == '+':
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = n2 * d1

    div = math.gcd(num, den)
    
    num_simplificado = num // div
    den_simplificado = den // div
    
    print(f"{num}/{den} = {num_simplificado}/{den_simplificado}")