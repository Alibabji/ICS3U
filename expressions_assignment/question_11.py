#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: simple_interest
#Description: calculates simple interested based on inputted value

principal=int(input("Enter the principal: "))
years=int(input("Enter the number of years: "))
interest=float(input("Enter the interest rate: "))
print(f"The value after the term is: ${principal*(1+years*interest):.2f}")