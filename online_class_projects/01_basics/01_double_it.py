def main():
    # Prompt the user to enter a starting number
    number = int(input("Give me a number, and I'll keep doubling it until we hit at least 100: "))
    
    # Keep doubling the number until it reaches or exceeds 100
    while number < 100:
        number *= 2
        print(number, end=" ")

    # Add a newline after the loop for cleaner output
    print()

# Entry point of the script
if __name__ == "__main__":
    main()
