def pairSum(sum_value, sorted_Arr):
    n = len(sorted_Arr)

    for i in range(n):
        for j in range(i + 1, n):
            if sorted_Arr[i] + sorted_Arr[j] == sum_value:
                return True
    return False
        

sum_value = int(input())
arr = sorted(list(map(int, input().split())))

print(pairSum(sum_value, arr))