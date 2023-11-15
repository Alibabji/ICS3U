import math
initial=int(input("Enter initial bacteria amount: "))
k=float(input("Enter constant value for k: "))
t=int(input("Enter the growth time period: "))
y=initial*math.exp(k*t)

print("{:.0f}".format(y),"bacteria will be present after {:.1f}".format(t),"hours.")