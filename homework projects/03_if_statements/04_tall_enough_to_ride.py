# Question 4: Height Requirement Checker for Ride

MIN_HEIGHT_CM = 50.0  # Minimum height in centimeters

def check_ride_eligibility():
    while True:
        entry = input("Enter your height in cm (press Enter to exit): ").strip()
        if not entry:
            break
        try:
            height = float(entry)
            if height >= MIN_HEIGHT_CM:
                print("✅ You're tall enough to ride!")
            else:
                print("❌ Not quite tall enough. Maybe next time!")
        except ValueError:
            print("⚠️ That wasn't a valid number. Try again!")

if __name__ == '__main__':
    check_ride_eligibility()
