__author__='Nick Jeong'
'''
November 15, 2023
math_computations
prints the sum, average (arithmetic mean), maximum, and minimum of the values entered
'''

sum_values = 0
count = 0
max_value = 0
min_value = float('inf')

while True:
    value = float(input("Enter a positive value(terminate with a negative value): "))

    if value < 0:
        break

    sum_values += value
    count += 1
    max_value = max(max_value, value)
    min_value = min(min_value, value)

average = sum_values / count if count > 0 else 0

print("\nSum: {:.2f}".format(sum_values))
print("Average: {:.2f}".format(average))
print("Maximum: {:.2f}".format(max_value))
print("Minimum: {:.2f}".format(min_value))
