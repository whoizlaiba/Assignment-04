# Question 3: Fruit Shop - Total Cost Calculator

def checkout_fruits():
    fruit_prices = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total = 0
    print("\n🍍 Welcome to the Fruit Stand!")
    for fruit in fruit_prices:
        try:
            qty = int(input(f"How many {fruit}s would you like? "))
            total += qty * fruit_prices[fruit]
        except ValueError:
            print("Invalid input, assuming 0.")

    print(f"\n🧾 Your total comes to: ${total:.2f}")

if __name__ == '__main__':
    checkout_fruits()
