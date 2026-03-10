s = input()
w = s.split()
r = ''
for i in range(len(w) - 1, -1, -1):
    r += w[i] 
    if i != 0:
        r += ' '
print(r)