a = str(input())
b = int(input())
r = ''
j = b - 1
while j < len(a):
    r += a[j]
    j += b
print(r)