# 🌀 Generate Fibonacci Numbers up to a Limit

LIMIT = 10000

def generate_fibonacci():
    a, b = 0, 1
    print("📘 Fibonacci numbers up to", LIMIT)
    while a <= LIMIT:
        print(a)
        a, b = b, a + b

if __name__ == '__main__':
    generate_fibonacci()
