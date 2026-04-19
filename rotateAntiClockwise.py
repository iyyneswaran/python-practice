def rotateAntiClockwise(matrix):
    length = len(matrix)

    # transpose
    for i in range(length):
        for j in range(i, length):
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the coloumn
    for i in range(length):
        for  j in range(length // 2):
            matrix[j][i], matrix[length - j - 1][i] = matrix[length - j - 1][i], matrix[j][i]

    return matrix
    
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(rotateAntiClockwise(matrix))