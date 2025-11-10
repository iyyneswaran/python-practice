b = []
bn = []
bs = []
for i in range(int(input())):
    b.append(input().strip())
for j in b:
    name, num = j.split(',')
    bn.append(name)
    bs.append(int(num))
ind = bs.index(max(bs))
print(bn[ind])
