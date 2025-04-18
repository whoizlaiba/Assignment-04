# Question 6: Square a Number

def square_value():
    print("== Question 6: Square Calculator ==")
    number = float(input("Enter a number to square: "))
    result = number ** 2
    print(f"{number} squared is {result}")

if __name__ == '__main__':
    square_value()
