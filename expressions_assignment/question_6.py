#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: div_and_mod
#Description: calculates result of integer and modulus division in either order.

num1=int(input("Enter an integer: "))
num2=int(input("Enter a second integer: "))
print(num1,"/",num2,"=",int(num1/num2))
print(num1,"%",num2,"=",int(num1%num2))
print(num2,"/",num1,"=",int(num2/num1))
print(num2,"%",num1,"=",int(num2%num1))