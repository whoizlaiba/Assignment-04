# Question 1: Add Multiple Numbers

def sum_all(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    values = [1, 2, 3, 4, 5]
    result = sum_all(values)
    print(f"The total sum is: {result}")

if __name__ == '__main__':
    main()
