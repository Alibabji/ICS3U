# Name: Nick Jeong
# Date: Oct 28th, 2023
# Program name: gallon_converter
# Description: displays the equivalent number of quarts, pints, cups, and tablespoons from gallons inputted

galon=int(input("Enter the number of gallons: "))
print(f"In {galon:.1f} gallons there are:")
print(f"{(galon*4):.1f} quarts\n{(galon*8):.1f} pints\n{(galon*16):.1f} cups\n{(galon*256):.1f} tablespoons")