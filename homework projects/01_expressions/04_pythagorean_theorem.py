# Question 4: Calculate Hypotenuse Using Pythagorean Theorem

import math

def find_hypotenuse():
    side_a = float(input("Length of side AB: "))
    side_b = float(input("Length of side AC: "))
    hypotenuse = math.sqrt(side_a**2 + side_b**2)
    print(f"Hypotenuse (BC) = {hypotenuse:.2f}")

if __name__ == '__main__':
    find_hypotenuse()
