s = str(input())

r = ''
n = ''
for i in s:
    if i.isdigit():
        n += i
    else:
        r += i * int(n)
        n = ''
print(r)