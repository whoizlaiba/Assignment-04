# Question 1: Print Even Numbers

def display_even_numbers():
    """Prints the first 20 even numbers in one line."""
    evens = [num * 2 for num in range(20)]
    print("Even numbers:", *evens)

if __name__ == '__main__':
    display_even_numbers()
