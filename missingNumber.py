arr = list(map(int, input().split()))
n = len(arr) + 1
total_sum = n * (n - 1) // 2
arr_sum = sum(arr)
missing_number = total_sum - arr_sum
print(missing_number)