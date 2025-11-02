a = str(input())
b = str(input())
same = []
for i in a:
    for x in b:
        if i == x:
            same.append(i)
result = []
for y in same:
    if y not in result:
        result.append(y)
print(len(result))