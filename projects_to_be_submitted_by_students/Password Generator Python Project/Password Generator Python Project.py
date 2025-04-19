import random

print("Welcome to Password Generator!")

keywords = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"


number = input("Amounts of passwords to generate: ")
number = int(number)
length = input("Input your passwords length: ")
length = int(length)

print("\nHere are your Passwords: ")


for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(keywords)
    print(password)