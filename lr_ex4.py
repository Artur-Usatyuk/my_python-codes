n = int(input("Ввудіть число n: "))
for i in range(10, 100):
    d1 = i // 10
    d2 = i % 10
    sum_of_squares = d1**2 + d2**2
    if sum_of_squares % n == 0:
        print(i, end="")