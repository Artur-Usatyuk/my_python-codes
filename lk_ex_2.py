number = int(input())
units = number % 10
tens = (number // 10) % 10
hundreds = number // 100
reversed_number = units * 100 + tens * 10 + hundreds
print(reversed_number)