import random

# Get user input
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Get computer choice
computer_choice = random.choice( ['rock', 'paper', 'scissors'])

# Print both choices
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Determine winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
