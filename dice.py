n = input()
dice =  [int(x) for x in n.split()]
x = int(input())
y = int(input())
bonus = 0
dec = 0
for i in dice:
    if i % 2 == 0:
        dec += y
    else:
        bonus += x
print(bonus - dec)