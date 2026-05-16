def next_permutation(n):
    digits = list(str(n))
    length = len(digits)

    # Step 1: find pivot
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # Step 2: if no pivot → reverse whole number
    if i == -1:
        digits.reverse()
        return int(''.join(digits))

    # Step 3: find next greater element
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 4: swap
    digits[i], digits[j] = digits[j], digits[i]

    # Step 5: reverse right part
    digits[i+1:] = reversed(digits[i+1:])

    return int(''.join(digits))


# Examples
print(next_permutation(12))   # 21
print(next_permutation(152))  # 215
print(next_permutation(321))  # 123