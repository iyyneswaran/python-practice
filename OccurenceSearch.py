string = str(input().strip())
a = str(input().strip())
b = str(input().strip())
count = 0
for i in range(len(string)-1):
    if string[i] == a and string[i+1] == b:
        count += 1
print(count)