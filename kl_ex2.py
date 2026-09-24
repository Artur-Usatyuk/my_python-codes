import sys
lines = sys.stdin.read().split()
for line in lines:
    if not line:
        continue
    num_str = line
    d1 = int(num_str[0])
    d2 = int(num_str[1])
    d3 = int(num_str[2])
    digit_sum_square = (d1 + d2 + d3) ** 2
    cudes_sum = d1**3 + d2**3 + d3**3
    if digit_sum_square == cudes_sum:
        print("True")
    else:
        print("False")