import sys
lines = [line.strip() for line in sys.stdin if line.strip()]
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        hours = int(lines[i])
        minutes = int(lines[i+1])
        total_minutes = hours * 60 + minutes
        print(total_minutes)