def odd_numbers(a, b):
    for i in range(a + 1, b):
        if i % 2 != 0:
            print(i, end=" ")
odd_numbers(int(input()), int(input()))