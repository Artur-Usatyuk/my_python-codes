s = int(input())
denominations = [500, 100, 10, 5, 1]
results = []
for bill in denominations:
    count = s // bill
    s %= bill
    results.append(f"{count} ({bill})")
print(", ".join(results))