# Name: Nick Jeong
# Date: Oct 28th, 2023
# Program name: project
# Description: calculates percentage of time taken for each part of the project

print("Enter the number of minutes spent on each of the following project tasks: ")
design=int(input("Designing: "))
code=int(input("Coding: "))
debug=int(input("Debugging: "))
test=int(input("Testing: "))
sum=design+code+debug+test
print("{:<10}".format("Task"), "{:>10}".format("% Time"))
print("{:<10}".format("Designing"), "{:>10}".format(f"{(design/sum*100):.2f}%"))
print("{:<10}".format("Coding"), "{:>10}".format(f"{(code/sum*100):.2f}%"))
print("{:<10}".format("Debugging"), "{:>10}".format(f"{(debug/sum*100):.2f}%"))
print("{:<10}".format("Testing"), "{:>10}".format(f"{(test/sum*100):.2f}%"))