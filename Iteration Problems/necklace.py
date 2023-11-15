__author__='Nick Jeong'
'''
November 15, 2023
neckalce
prompts the user for two single-digit integers and then displays the sequence and the number of steps taken
'''

num1 = int(input("Enter the first starting number: "))
num2 = int(input("Enter the second starting number: "))

sequence = [num1, num2]
steps = 0

current_num1, current_num2 = num1, num2
steps = 0

print(current_num1, end=" ")
print(current_num2, end=" ")

while current_num1 != num1 or current_num2 != num2 or steps == 0:
    next_num = (current_num1 + current_num2) % 10
    print(next_num, end=" ")

    current_num1, current_num2 = current_num2, next_num
    steps += 1


