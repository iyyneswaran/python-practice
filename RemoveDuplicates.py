arr = list(map(int, input().split()))

res = []

for num in arr:
    if num not in res:
        res.append(num)

print(res)