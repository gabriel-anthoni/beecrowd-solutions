import bisect

loop = 1
while True:
    marbles = []
    numbers = input().split()
    if numbers[0] == "0" and numbers[1] == "0":
        break
    for _ in range(int(numbers[0])):
        marbles.append(int(input()))
    print(f"CASE# {loop}:")
    marbles.sort()
    loop += 1
    for _ in range(int(numbers[1])):
        query = int(input())
        pos = bisect.bisect_left(marbles, query)
        if pos < len(marbles) and marbles[pos] == query:
            print(f"{query} found at {pos+1}")
        else:
            print(f"{query} not found")