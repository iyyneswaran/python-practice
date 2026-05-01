# manual conversion
def conversion(number, base):
    result = 0
    power = 0
    for digit in reversed(number):
        result += int(digit) * (base ** power)
        power += 1
    return result


n = int(input())
x, y = input().split()
print(conversion(x, n) + conversion(y,n))



# built in function
base_n = int(input().strip())
x_n, y_n = input().split()

x_dec = int(x_n, n)
y_dec = int(y_n, n)

print(x_dec + y_dec)