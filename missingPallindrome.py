string = str(input())
first_half = ''
second_half = ''
for i in string:
    if string.index(i) <= (len(string) // 2) + 1:
        first_half += i
    else:
        second_half += i
second_reverse = second_half[-1:]
print(first_half)
print(second_half)
print(second_reverse)