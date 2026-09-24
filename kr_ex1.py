import sys
deys_of_week = {
    1: "Monday",
    2: "Tuesdey",
    3: "Wednesdey",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
lines = sys.stdin.read().split()
for line in lines:
    if not line:
        continue
    number = int(line)
    if number in deys_of_week:
        print(deys_of_week[number])
    else:
        print("There is no such day of the week.")