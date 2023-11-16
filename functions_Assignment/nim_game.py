__author__='Nick Jeong'
'''
November 12, 2023
nim_game
game that computer and user takes rock
'''
import random

stoneNum=random.randint(15,30)
num = int()
turn = 0

def is_valid_entry(entry=int()):
    global stoneNum,turn # uses global variable stoneNum
    if entry>0 and entry<4:
        stoneNum-= entry # subtract stoneNum by inputted value
        turn+=1 
    else:
        print("ERROR!! Please enter integer between 1 and 3!!!")

def draw_stones():
    global num, stoneNum, turn
    if stoneNum<=2:
        num=random.randint(1,2)
    elif stoneNum==1:
        num=1
    else:
        num=random.randint(1,3)
    print("The computer takes {} stones.".format(num))
    stoneNum-=num
    turn+=1

# main function
while stoneNum>0:
    print("There are {} stones".format(stoneNum),end=' ')
    if turn%2==0:
        num=int(input("How many would you like? "))
        is_valid_entry(num)
    else:
        draw_stones()

if turn%2==0:
    print("The Computer beats the Player!")
else:
    print("The Player beats the Computer!")
