arr = list(map(int, input().split()))

sorted_Arr = sorted(arr)

new_Arr = []
for i in sorted_Arr:
    if i not in new_Arr:
        new_Arr.append(i)

res = []
for val in arr:
    rank = len(new_Arr) - new_Arr.index(val)
    res.append(rank)

print(*res)