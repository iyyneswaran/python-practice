def position(x, y, directions):
    updated_x = int(x)
    updated_y = int(y)

    for i in directions:
        direction = i[0].upper()
        distance = int(i[1:])
        if len(i) > 1 and i[1:].isdigit():
            if direction == 'N':
                updated_y += distance
            elif direction == 'S':
                updated_y -= distance
            elif direction == 'E':
                updated_x += distance
            elif direction == 'W':
                updated_x -= distance

    return "x" + str(updated_x) + " " + "y" + str(updated_y)


initial_direction = input().split()
directions = initial_direction[2:]
xval, yval = initial_direction[0], initial_direction[1]
initial_X = xval[1:]
initial_Y = yval[1:]

print(position(initial_X, initial_Y, directions))