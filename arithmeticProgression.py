a1, a2, a3 = map(int, input().split())
n = int(input())
d = a2 - a1
nth = a1 + (n-1) * d
print(nth)
