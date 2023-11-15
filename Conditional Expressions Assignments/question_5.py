import math

a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))
c=int(input("Enter value for c: "))
if b**2-(4*a*c)<0:
    print("ERROR!! Non real roots exist!!")
else:
    print("The roots are ","{:.1f}".format((-b+math.sqrt(b**2-(4*a*c)))/(2*a)),"and {:.1f}".format((-b-math.sqrt(b**2-(4*a*c)))/(2*a)))