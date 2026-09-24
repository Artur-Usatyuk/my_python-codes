import sys
lines = sys.stdin.read().split()
for line in lines:
    if not line:
        continue
    t = int(line)
    remainder = t % 6
    if remainder <= 3:
        print("green")
    elif remainder == 4:
        print("yellow")
    else:
        print("red")