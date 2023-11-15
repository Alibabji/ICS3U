#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: change
#Description: calculates minimum number of coins necessary to make the change

change = int(input("Enter the change in cents: "))
quarter=25
dime = 10
nickel=5
penny=1;
if change>0:
    print("The minimum number of coins is: \n")
    print("Quarters: ",int(change/quarter))
    change%=quarter;
    print("Dimes: ", int(change / dime))
    change%=dime
    print("Nickels: ", int(change / nickel))
    change%=nickel
    print("Pennies: ", int(change))