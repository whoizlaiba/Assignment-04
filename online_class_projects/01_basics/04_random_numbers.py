import random

def create_random_list(total=10, low=1, high=100):
    """
    Create a list of random numbers within a given range.

    Parameters:
    - total (int): How many numbers to generate.
    - low (int): Minimum value (inclusive).
    - high (int): Maximum value (inclusive).

    Returns:
    - list[int]: A list of random integers.
    """
    return [random.randint(low, high) for _ in range(total)]

def main():
    numbers = create_random_list()
    print("🔢 Here are your random numbers:")
    print(", ".join(str(num) for num in numbers))

if __name__ == "__main__":
    main()
