a = str(input())
b = str(input())
r = ''
for i in a:
    if i in b and i not in r:
        r += i
print(r)