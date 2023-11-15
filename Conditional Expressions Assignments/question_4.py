import math

print("Rectangular Prism")
l=int(input("Enter the Length: "))
w=int(input("Enter the Width: "))
h=int(input("Enter the Height: "))
print("The volume is: ",l*w*h)

print("Sphere")
r=int(input("Enter the Radius: "))
d=2*r
print("The volume is: ","${:.3f}".format((math.pi*(d**3))/6))

print("Cube")
s=int(input("Enter the length of each side: "))
print("The volume is: ",s**3)
