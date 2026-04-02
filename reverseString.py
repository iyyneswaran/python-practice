# Reverse a string using for loop
def ReverseString(word):
    result = ''
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result

print(ReverseString(str(input())))

# reverse a string using traversing by setting the step index to -1
def ReverseStringByTraversing(word):
    return word[::-1]
print(ReverseStringByTraversing(str(input())))