n = int(input())
a = []
f = []
s = []
for i in range(n):
    a.append(input().strip())
for j in a:
    first, second = j.split(' ')
    f.append(first)
    s.append(second)
f_avg = 0
s_avg = 0
for k in f:
    f_avg += int(k)
for l in s:
    s_avg += int(l)
avg_f = f_avg / n
avg_s = s_avg / n
print("%.2f" % avg_f)
print("%.2f" % avg_s)