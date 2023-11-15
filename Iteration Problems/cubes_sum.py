__author__='Nick Jeong'
'''
November 12, 2023
cubes_sum
prompts the user for a non-negative integer and then displays the sum of the cubes of the digits
'''

num = int(input("Enter a positive integer: "))
cubes_sum = 0
divisor = 1

while num // divisor >= 10:
    divisor *= 10

while divisor > 0:
    digit = num // divisor
    cubes_sum += digit ** 3
    num %= divisor
    divisor //= 10

print("The sum of the cubes of the digits is: {}".format(cubes_sum))