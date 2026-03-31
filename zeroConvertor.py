n = int(input())

def check(n):
    if n == 0:
        print("already Zero")
    elif n > 0:
        pos(n)
    else:
        neg(n)

def pos(n):
    for i in range(n, -1, -1):
        print(i, end=" ")
    
def neg(n):
    for i in range(n, 1):
        print(i, end=" ")
    
