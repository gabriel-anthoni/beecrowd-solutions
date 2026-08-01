positive = 0
for _ in range(6):
    number = float(input())
    if number > 0:
        positive += 1
print(f"{positive} valores positivos")