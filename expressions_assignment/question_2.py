#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: pizza_cost
#Description: calculates total price of the pizza by its diameter

labor_cost=0.75
rent_cost=1.00
diameter = float(input("Enter the diameter of the pizza in inches: "))
if diameter>0:
    materials_cost = 0.05 * diameter * diameter
    cost=labor_cost+rent_cost+materials_cost
    print(f"The cost of making the pizza is: ${cost:.2f}")
else:
    print("ERROR!! Invalid input!!!")