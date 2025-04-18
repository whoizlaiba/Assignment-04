# ➗ Double a Number Until It Exceeds 100

def double_up():
    try:
        start = int(input("Enter a starting number: "))
        print("🔁 Doubling until we pass 100:")
        while start <= 100:
            start *= 2
            print(start, end=" ")
    except ValueError:
        print("❌ Please input a valid number.")

if __name__ == '__main__':
    double_up()
