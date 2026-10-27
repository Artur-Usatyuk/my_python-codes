number_str = input("Enter a float number: ")
dot_index = number_str.find('.')
first_digit_after_dot = number_str[dot_index + 1]
print(first_digit_after_dot)