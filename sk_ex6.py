roman_str = input("Enter Roman numeral: ").upper()
roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
decimal_value = 0
n = len(roman_str)
for i in range(n):
    current_val = roman_map[roman_str[i]]
    if i + 1 < n and current_val < roman_map[roman_str[i + 1]]:
        decimal_value -= current_val
    else:
        decimal_value += current_val
print(decimal_value)