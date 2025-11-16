n = int(input())

m = [] 
for i in range(n):   
    row = list(map(int, input().split()))
    m.append(row)

print(m)
 
# it's simple one liner to get the sum of corner elements of square matrix
# sum_value = m[0][0] + m[0][n-1] + m[n-1][0] + m[n-1][n-1]

# if u wanna use loop then below is the code
# i prefer harder one hehehe
sum_value = 0
for i in range(n):
    for j in range(n):
        if (i == 0 and j ==0) or (i == 0 and j == n - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == n -1):
            sum_value += m[i][j]

print(sum_value)