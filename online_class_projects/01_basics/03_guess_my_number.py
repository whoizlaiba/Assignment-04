import random

def main():
    # Randomly pick a number between 1 and 99
    hidden_number = random.randint(1, 99)
    
    print("🎲 I'm thinking of a number between 1 and 99. Can you guess what it is?")
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Your guess: "))
            
            if guess < hidden_number:
                print("Too low! Try a higher number.")
            elif guess > hidden_number:
                print("Too high! Go a bit lower.")
            else:
                print(f"🎉 Nice job! You guessed it right. The number was {hidden_number}.")
                break  # Exit the loop when the correct guess is made
            
            print()  # Just to keep things tidy in the output
            
        except ValueError:
            print("🚫 Please enter a valid number.\n")

# Start the game
if __name__ == '__main__':
    main()
