# Question 3: Leap Year Checker

def is_leap(year: int) -> bool:
    """Return True if the year is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    try:
        input_year = int(input("Enter a year: "))
        if is_leap(input_year):
            print(f"{input_year} is a leap year! 🎉")
        else:
            print(f"{input_year} is not a leap year.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid year.")

if __name__ == '__main__':
    main()
