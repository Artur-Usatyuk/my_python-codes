prev = int(input())
sign_changes = 0
if prev != 0:
    while True:
        current = int(input())
        if current == 0:
            break
        if prev * current < 0:
            sign_changes += 1
        prev = current
print(sign_changes)