import sys
lines = [line.strip() for line in sys.stdin if line.strip()]
if len(lines) >= 2:
    s = lines[0]
    sub = lines[1]
    positions = []
    start = 0
    while True:
        pos = s.find(sub, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1 
    if positions:
        print(*(positions))
    else:
        print(-1) 