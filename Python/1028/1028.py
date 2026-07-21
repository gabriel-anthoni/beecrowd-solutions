import math

lines = int(input())
for _ in range(lines):
    cards    = input().split()
    f1       = int(cards[0])
    f2       = int(cards[1])
    print(math.gcd(f1, f2))