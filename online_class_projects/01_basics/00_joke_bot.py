# Program Constants
PROMPT: str = "Hey there! What can I do for you? "
JOKE: str = "Sure thing! 🤣 Why do developers love dark mode? Because light attracts bugs!"
DEFAULT_REPLY: str = "Hmm... I only specialize in jokes for now!"

def main():
    # Get input from the user
    user_request = input(PROMPT)

    # Clean up the input: remove extra spaces and make it lowercase
    user_request = user_request.strip().lower()

    # Respond based on the user's input
    if user_request == "joke":
        print(JOKE)
    else:
        print(DEFAULT_REPLY)

# Run the program
if __name__ == "__main__":
    main()
