expr = input().strip()

if '+' in expr:
    a, rest = expr.split('+')
    op = '+'
elif '-' in expr:
    a, rest = expr.split('-')
    op = '-'
elif '*' in expr:
    a, rest = expr.split('*')
    op = '*'
else:
    a, rest = expr.split('/')
    op = '/'

b, c = rest.split('=')
a, b, c = int(a), int(b), int(c)

if a + b == c:
    print('+')
elif a - b == c:
    print('-')
elif a * b == c:
    print('*')
elif b != 0 and a / b == c:
    print('/')
