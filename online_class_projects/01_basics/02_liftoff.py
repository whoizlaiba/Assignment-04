import random

def main():
    # Secret number randomly chosen between 1 and 99
    target = random.randint(1, 99)

    print("🤔 I'm thinking of a number between 1 and 99.")
    
    # Start the guessing game
    while True:
        try:
            guess = int(input("Take a guess: "))
            
            if guess < target:
                print("Too low! Try a bit higher. 🔼")
            elif guess > target:
                print("Too high! Try something lower. 🔽")
            else:
                print(f"🎉 Nailed it! The number was {target}.")
                break

            print()  # Adds a blank line for better readability

        except ValueError:
            print("Oops! Please enter a valid number.\n")

# Run the game
if __name__ == "__main__":
    main()
