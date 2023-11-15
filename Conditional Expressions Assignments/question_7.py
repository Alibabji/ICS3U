p=int(input("Principal: "))
r=float(input("Ineterest rate: "))
m=int(input("Number of monthly payments: "))

payment=(p*(r/12))/(1-(1+r/12)**(-m))

print("The monthly payment is: ${:.2f}".format(payment))