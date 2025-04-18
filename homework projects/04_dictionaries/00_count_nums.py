# Question 1: Number Frequency Tracker

def track_number_frequency():
    print("\n📈 Frequency Counter - Start entering numbers!")
    print("➤ Press Enter without typing a number to stop.\n")

    number_counts = {}

    while True:
        entry = input("Enter a number: ").strip()
        if entry == "":
            break
        try:
            num = int(entry)
            number_counts[num] = number_counts.get(num, 0) + 1
        except ValueError:
            print("⚠️ Please enter a valid integer.")

    print("\n📊 Frequency Summary:")
    if number_counts:
        for key in sorted(number_counts.keys()):
            print(f"🔸 {key} → {number_counts[key]} time(s)")
    else:
        print("No input recorded.")

if __name__ == '__main__':
    track_number_frequency()
