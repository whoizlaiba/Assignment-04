# Question 5: Random Number Generator

import random

def generate_random_numbers():
    count = 10
    low, high = 1, 100
    numbers = [random.randint(low, high) for _ in range(count)]
    print("Generated numbers:", " ".join(map(str, numbers)))

if __name__ == '__main__':
    generate_random_numbers()
