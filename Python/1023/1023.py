import sys

city = 1

while True:
    line = sys.stdin.readline()
    if not line:
        break

    houses = int(line.strip())
    if houses == 0:
        break

    total_people = 0
    total_consumption = 0
    consumptions = {}

    for _ in range(houses):
        line = sys.stdin.readline().strip()
        people, consumption = map(int, line.split())

        total_people += people
        total_consumption += consumption

        avg = consumption // people
        consumptions[avg] = consumptions.get(avg, 0) + people

    print(f"Cidade# {city}:")
    city += 1

    for key in sorted(consumptions):
        print(f"{consumptions[key]}-{key}", end=" ")
    print()

    avg_consumption = (total_consumption * 100) // total_people
    avg_consumption = avg_consumption / 100

    print(f"Consumo medio: {avg_consumption:.2f} m3.")
    print()