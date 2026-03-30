def UpperCaseLettersCount(word):
    count = 0
    for i in word:
        if i.isupper():
            count += 1
    return count

print(UpperCaseLettersCount(str(input())))