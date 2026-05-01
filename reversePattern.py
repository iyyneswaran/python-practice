def reversePattern(matrix):
    n = len(matrix)
    for i in range(n):
        end = n - i
        if n - i >= n - 2:
            for j in range(i, end):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


n = int(input())
matrix = []
start = (n * (n + 1)) // 2
for i in range(n):
    row = []
    end = start - (n - i)
    for j in range(start, end, -1):
        row.append(j)

    start = end
    matrix.append(row)

print(matrix)


print(reversePattern(matrix))

for row in matrix:
    print(*row)