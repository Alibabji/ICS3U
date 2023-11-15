#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: object_height
#Description: calculates height by using h=100-4.9t^2 formula

time=float(input("Enter a time less than 4.5 seconds: "))
if 0<=time<4.5:
    height=100-4.9*time**2
    print(f"The height of the object is: {height:.1f} metres.")
else:
    print("ERROR!! Invalid input!!!")