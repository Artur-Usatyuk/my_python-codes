import sys
input_data = sys.stdin.read().split()
if input_data:
    k = int(input_data[0])
    for x in range(1, k + 1):
        n = int(input_data[x])
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if s == s[::-1]:
                count += 1
        print(count)