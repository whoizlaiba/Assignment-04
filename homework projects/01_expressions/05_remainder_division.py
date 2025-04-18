# Question 5: Division and Remainder

def divide_numbers():
    num1 = int(input("Enter the dividend: "))
    num2 = int(input("Enter the divisor: "))
    quotient = num1 // num2
    remainder = num1 % num2
    print(f"{num1} divided by {num2} gives {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    divide_numbers()
