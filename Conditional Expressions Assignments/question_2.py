weight=int(input("Enter package weight in kilograms: "))
lentgh=int(input("Enter package length in centimeters: "))
width=int(input("Enter package width in centimeters: "))
height=int(input("Enter package height in centimeters: "))

if weight>27:
    print("Too heavy",end=' ')
    if lentgh*width*height>100000:
        print("and too large")
elif lentgh*width*height>100000:
    print("Too large")
else:
    print("Package meets the requirements")