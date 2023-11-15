import math
x=int(input("Enter a value for X: "))
y=int(input("Enter a value for Y: "))
formula=math.exp(y*math.log(x,math.e))
print("The results from using the formula is: ", formula)
function=math.pow(x,y)
print("The reuslts from using the Math pow() method is: ", function)