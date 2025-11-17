# pure logic to count prime numbers in a given range
import math
n1 = int(input())
n2 = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

count = 0
for num in range(n1, n2 + 1):
    if is_prime(num):
        count += 1

print(count)





# library to check prime numbers efficiently
# from sympy import isprime
# starting_number = int(input())
# ending_number = int(input())
# count = 0
# for i in range(starting_number, ending_number + 1):
#     if isprime(i):
#         count += 1
# print(count)