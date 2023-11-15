__author__='Nick Jeong'
'''
November 12, 2023
digits_sum
prompts the user for a non-negative integer and then displays the sum of the digits.
'''
num = int(input("Enter a positive integer: "))
digit_sum = 0
divisor = 1

while num // divisor >= 10:
    divisor *= 10

while divisor > 0:
    digit = num // divisor
    digit_sum += digit
    num %= divisor
    divisor //= 10

print("The sum of the digits is: {}".format(digit_sum))