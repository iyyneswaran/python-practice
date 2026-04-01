arr = tuple(map(int, input().split()))
result = 0
checking_Arr = []
for i in arr:
    if i in checking_Arr:
        result = 1
    checking_Arr.append(i)
if result == 0:
    print("True")
else:
    print("False")