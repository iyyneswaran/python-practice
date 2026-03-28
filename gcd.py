# Basic GCD Algorithm [not optimized]

a = int(input())
b = int(input())
a1 = []
b1 = []
f = []
for i in range(1, a+1):
    if a % i == 0:
        a1.append(i)
for i in range(1, b+1):
    if b % i == 0:
        b1.append(i)
for k in range(len(a1)):
    if a1[k] in b1:
        f.append(a1[k])
print(max(f))