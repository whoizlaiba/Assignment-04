def subtract_seven(number):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return number - 7

def main():
    original_value = 7
    result = subtract_seven(original_value)
    print("This should be zero:", result)

# This ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
