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
    if entry>0 and entry<4:
        stoneNum-=num
        return true
    else:
        print("ERROR!! Please enter integer between 1 and 3!!!")
        return false

def draw_stones():
    num=random.randint(1,3)
    print("The computer takes {} stones.".format(num))
    stoneNum-=num

# main function
while stoneNum>0:
    print("There are {} stones".format(stoneNum),end=' ')
    if turn%2==0:
        num=int(input("How many would you like? "))
        is_valid_entry(num)
    else:
        draw_stones()
    turn+=1

if turn%2==0:
    print("The Computer beats the Player!")
else:
    print("The Player beats the Computer!")
