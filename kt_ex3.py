import sys
lines = sys.stdin.read().split()
for line in lines:
    if not line:
        continue
    year = int(line)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year.")
    else:
        print("Ordinary year.")