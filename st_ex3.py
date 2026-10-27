n = int(input("Enter n: "))
terms = []
total_sum = 0
for i in range(1, n):
    terms.append(f"{i}*{i+1}")
    total_sum += i * (i +1)
expression_str = "+".join(terms)
result_str = f"{expression_str}={total_sum}"
print(result_str)