def rightAngleTriangle(n):
    for i in range(1, n + 1):
        print("* " * i)

rightAngleTriangle(int(input("Right Angle Triangle: ")))



def invertedRightAngleTriangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

invertedRightAngleTriangle(int(input("Inverted Right Angle Triangle: ")))