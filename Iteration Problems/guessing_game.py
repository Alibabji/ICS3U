__author__='Nick Jeong'
'''
November 12, 2023
digits_sum
Guessing Game program that asks the user for an integer from 1 - 50. The  program will say too high or too low.'''
import random

low=1
high=50

num = random.randint(low, high)
player_guess = 0

while player_guess != num:
    player_guess = int(input("Enter your guess: "))

    print("Current Low: {}\tCurrent High: {}\tPlayer Types: {}".format(low, high, player_guess),end='   ')

    if player_guess < num:
        print('{:>8}'.format("Too low."))
        low = player_guess + 1
    elif player_guess > num:
        print('{:>8}'.format("Too high."))
        high = player_guess - 1
    else:
        print('{:>8}'.format("You guessed it!"))