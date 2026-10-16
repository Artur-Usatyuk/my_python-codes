n = int(input())
for i in range(1, n + 1):
    row_elements = []
    for j in range(i, n + 1):
        row_elements.append(str(j))
    print("\t".join(row_elements))
    