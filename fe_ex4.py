import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    cities = [city.strip() for city in line.split(',')]

    if len(cities) > 1:
        result = ", ".join(cities[:-1]) + " and " + cities[-1]
    else:
        result = cities[0]

    print(result)