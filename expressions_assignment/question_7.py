#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: order
#Description: calculates tax and final price of food ordered

bp=float(1.69)
fp=float(1.09)
sp=float(0.99)
burgerNum=int(input("Enter the number of burgers: "))
friesNum=int(input("Enter the number of fries: "))
sodaNum=int(input("Enter the number of sodas: "))
totalprice=burgerNum*bp+friesNum*fp+sodaNum*sp
tax=totalprice*0.065
print(f"Total before tax: ${totalprice:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Final total: ${totalprice+tax:.2f}")