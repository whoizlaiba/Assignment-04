# Question 2: International Voting Age Checker

MIN_AGE_NEO = 16     # NeoLand
MIN_AGE_ELDO = 25    # Eldoria
MIN_AGE_GRAY = 48    # Grayshore

def check_eligibility():
    try:
        age = int(input("Please enter your age: "))
        
        if age >= MIN_AGE_NEO:
            print(f"✅ You can vote in NeoLand (min age {MIN_AGE_NEO})")
        else:
            print(f"❌ You can't vote in NeoLand (min age {MIN_AGE_NEO})")

        if age >= MIN_AGE_ELDO:
            print(f"✅ You can vote in Eldoria (min age {MIN_AGE_ELDO})")
        else:
            print(f"❌ You can't vote in Eldoria (min age {MIN_AGE_ELDO})")

        if age >= MIN_AGE_GRAY:
            print(f"✅ You can vote in Grayshore (min age {MIN_AGE_GRAY})")
        else:
            print(f"❌ You can't vote in Grayshore (min age {MIN_AGE_GRAY})")

    except ValueError:
        print("⚠️ Please enter a valid numeric age.")

if __name__ == '__main__':
    check_eligibility()
