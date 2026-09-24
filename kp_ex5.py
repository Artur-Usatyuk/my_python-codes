import sys
lines = sys.stdin.read().split()
if len(lines) >= 4:
    x1 = int(lines[0])
    y1 = int(lines[1])
    x2 = int(lines[2])
    y2 = int(lines[3])
    if x1 == x2 or y1 == y2:
        print("yes")
    else:
        print("no")