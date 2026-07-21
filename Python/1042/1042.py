numbers = input().split()
numbers = [ int(number) for number in numbers ]
newNumbers = []
newNumbers.append(sorted(numbers))
for _ in range(len(newNumbers[0])):
    print(newNumbers[0][_])
print()
for _ in numbers:
    print(_)