import sys
for line in sys.stdin:
    binary_str = line.strip()
    if not binary_str:
        continue
    try:
        decimal_number = int(binary_str, 2)
        print(decimal_number)
    except ValueError:
        break