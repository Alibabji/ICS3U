#Name: Nick Jeong
#Date: Oct 28th, 2023
#Program name: energy
#Description: calculates energy and etc.

mass = float(input("Enter the mass in kilograms: "))
c=3.0e8 # speed of light
energy=mass*c**2
lightbulb=energy/360000
print(f"The energy produced in joules is = {energy:.1E}")
print(f"The number of 100-watt light bulbs powered = {lightbulb:.1E}")
