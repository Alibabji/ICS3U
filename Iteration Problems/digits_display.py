__author__='Nick Jeong'
'''
November 12, 2023
digits_display
prompts the user for a non-negative integer and then displays each digit on a separate line
'''
num = int(input("Enter a positive integer: "))
divisor = 1
while num // divisor >= 10:
     divisor *= 10
while divisor > 0:
    digit = num // divisor
    print("{:d}".format(digit))
    num %= divisor
    divisor //= 10