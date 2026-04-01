def stringJumper(x):
    for i in range(0, len(x)):
        if i % 2 == 0:
            print(x[i], end="")
stringJumper(str(input()))