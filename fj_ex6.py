import sys
input_data = sys.stdin.read().split()
if len(input_data) >= 3:
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    total = a + b + c
    if total % 3 != 0:
        print("NO SOLUTIONS")
    else:
        target = total // 3
        moves = 0
        if a > target:
            moves += a - target
        if b > target:
            moves += b - target
        if c > target:
            moves += c - target
        print(moves)