def SecondLargestNumber(n):
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    return sorted(numbers)[1]
print(SecondLargestNumber(int(input())))