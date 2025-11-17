s = input().strip().split()
result = []
for word in s:
    new = ''
    for i in range(len(word)):
        if i % 2 == 0:
            new += word[i].upper()
        else:
            new += word[i].lower()
    result.append(new)
print(' '.join(result))