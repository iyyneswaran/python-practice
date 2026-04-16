def smallMatrix(n, m, big, small):
    for i in range(n - m + 1):
        for j in range(n -m + 1):
            match = True
            for x in range(m):
                for y in range(m):
                    if big[i + x][j + y] != small[x][y]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return "TRUE"
    return "FALSE"

n = int(input())
m = int(input())
n_matrix = []
m_matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    n_matrix.append(row)

for _ in range(m):
    row = list(map(int, input().split()))
    m_matrix.append(row)

print(smallMatrix(n, m, n_matrix, m_matrix))