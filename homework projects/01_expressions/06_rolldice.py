# Question 6: Rolling Two Dice

import random

def roll_two_dice():
    sides = 6
    roll1 = random.randint(1, sides)
    roll2 = random.randint(1, sides)
    print(f"Each die has {sides} sides.")
    print(f"Roll 1: {roll1}, Roll 2: {roll2}, Total: {roll1 + roll2}")

if __name__ == '__main__':
    roll_two_dice()
