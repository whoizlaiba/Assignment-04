# 🎯 Guess the Secret Number Game

import random

def guess_the_number():
    print("🔢 Welcome to the Guessing Game!")
    secret = random.randint(1, 100)
    guess = None

    while guess != secret:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < secret:
                print("📉 Too low, try again!")
            elif guess > secret:
                print("📈 Too high, try again!")
        except ValueError:
            print("❌ Please enter a valid number.")

    print(f"🎉 Nice job! The secret number was {secret}.")

if __name__ == '__main__':
    guess_the_number()
