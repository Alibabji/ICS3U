#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: digits
#Description: prints out each digit of inputted number

number = int(input("Enter a three-digit number: "))
hd=int(number/100)
number-=hd*100
td=int(number/10)
number-=td*10
print("The hundreds-place digit is: ", int(hd))
print("\n The tens-place digit is: ", int(td))
print("\n The ones-place digit is: ", int(number))
