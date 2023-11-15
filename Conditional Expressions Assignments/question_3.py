num=int(input("Enter the number of eggs purchased: "))
price=0;
if num/12>=11:
    price=float(0.35/12*num)
elif num/12>=6:
    price=float(0.40/12*num)
elif num/12>=4:
    price=float(0.45/12*num)
else:
    price=float(0.50/12*num)
print("The bill is equal to: ", "${:.2f}".format(price))