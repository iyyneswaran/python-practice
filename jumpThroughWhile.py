def printIncreasringPower(x):
    # code 
    i = 1
    sv = 1
    while(sv <= x):
        print(i ** 2, end=" ")
        i += 1
        sv = i ** 2
        # code 
printIncreasringPower(int(input()))