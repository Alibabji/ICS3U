# Name: Nick Jeong
# Date: Oct 28th, 2023
# Program name: spending
# Description: calculates percentage of expenditures in each category

print("Enter the amount spent last month on the following items:")

food=int(input("Food: $"))
cloth=int(input("Clothing: $"))
entertain=int(input("Entertaining: $"))
rent=int(input("Rent: $"))

sum=food+cloth+entertain+rent

print("{:<15}".format("Category"), "{:>10}".format("Budget"))
print("{:<15}".format("Food"), "{:>10}".format(f"{(food/sum*100):.2f}%"))
print("{:<15}".format("Clothing"), "{:>10}".format(f"{(cloth/sum*100):.2f}%"))
print("{:<15}".format("Entertaining"), "{:>10}".format(f"{(entertain/sum*100):.2f}%"))
print("{:<15}".format("Rent"), "{:>10}".format(f"{(rent/sum*100):.2f}%"))