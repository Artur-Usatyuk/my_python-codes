import sys
lines =sys.stdin.read().split()
for line in lines:
    if not line:
        continue
    n = int(line)
    last_digit = n % 10
    last_two_digits = n % 100
    if 11 <= last_two_digits <= 14:
        print(f"{n} rokiv")
    elif last_digit == 1:
        print(f"{n} rik")
    elif 2 <= last_digit <= 4:
        print(f"{n} zoku")
    else:
        print(f"{n} rokiv")