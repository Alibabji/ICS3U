__author__='Nick Jeong'
'''
November 12, 2023
digits_sum
Have the application average 50 trials, and display the average and the greatest number of steps.'''

import random

position=3.5
count=0
steps=0
maxsteps=0
sum=0

while count<50:
    while position > 0 and position < 7:
        num=random.choice([1,-1])
        if num==1:
            position +=1
            steps+=1
        if num == -1:
            position -=1
            steps+=1
    count+=1
    sum+=steps

    if steps > maxsteps:
        maxsteps = steps
    position = 3.5
    steps = 0

print("average number of steps: ", sum/50)
print("Max number of steps: ", maxsteps)