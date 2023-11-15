copy=int(input("Enter the number of copies to be printed: "))
price = 0
print("Price per copy is: ", end = '')

if copy>1000:
    price=0.25
elif copy>750:
    price = 0.26
elif copy>500:
    price = 0.27
elif copy>100:
    price = 0.28
else:
    price=0.30

print("${:.2f}".format(price),"\nTotal cost is: ", "{:.2f}".format(copy*price))