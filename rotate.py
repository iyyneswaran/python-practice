def rotateMatrix(matrix):
    lenght = len(matrix)

    for i in range(lenght):
        for j in range(i, lenght):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(rotateMatrix(matrix))