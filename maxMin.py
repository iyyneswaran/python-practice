def maxMin(arr):
    maxValue = 0
    minValue = arr[0]
    result = []
    for i in range(0, len(arr), 1):
        if arr[i] > maxValue:
            maxValue = arr[i]
        if arr[i] < minValue:
            minValue = arr[i]
    result.append(minValue)
    result.append(maxValue)
    return result

arr = [4,6,7,8,2,3,5,34,54,64]
print(maxMin(arr))