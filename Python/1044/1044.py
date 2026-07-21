numbers = input().split()
numbers = [ int(number) for number in numbers ]
if (max(numbers) % min(numbers)) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")