n = input()
while True:
    password_attempt = input()
    if password_attempt == n:
        print(n)
        print("Done")
        break
    else:
        print(password_attempt)
        print("Error")