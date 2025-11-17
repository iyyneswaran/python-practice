string = str(input().strip())
n = int(input())
print((string[len(string) - n : ]) + (string[0:len(string) - n]))