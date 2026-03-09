try:
    user_input = input("Enter string and target character: ").split(None, 1)
    if len(user_input) < 2:
        print("Error: Please enter both a string and a character.")
    else:
        s, c = user_input
        r = ''
        for i in s:
            if i == c:
                break
            r += i
        print(r)
except ValueError:
    print("Invalid input format.")