import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    number = int(line)
    digit_count = len(str(abs(number)))
    if digit_count < 7:
        stars = '*' * (7 - digit_count)
        print(f"{number}{stars}")
    else:
     print(number) 