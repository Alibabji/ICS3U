import math
angle=int(input("Enter an angle in degrees: "))
atr=math.radians(angle) # convert degree too radians
print("\nSin(",angle,") = {:.4f}".format(math.sin(atr)))
print("Cos(",angle,") = {:.4f}".format(math.cos(atr)))
print("Tan(",angle,") = {:.4f}".format(math.tan(atr)))