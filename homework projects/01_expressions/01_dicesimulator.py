# Question 1: Dice Simulator

import random

def simulate_dice_roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    print(f"Rolled total: {result}")

def main():
    test_die = 10
    print(f"Starting test_die in main: {test_die}")
    for _ in range(3):
        simulate_dice_roll()
    print(f"Value of test_die after rolls: {test_die}")

if __name__ == '__main__':
    main()
