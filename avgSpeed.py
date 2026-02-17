l = str(input())
s = l.split()
speed, time = 0, 0 
for i in s:
    split_i = i.split('@')
    speed += int(split_i[0])
    time += int(split_i[1])
print(f'{speed/time:.2f}')
