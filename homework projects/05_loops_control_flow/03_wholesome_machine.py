# 🌟 Wholesome Affirmation Repeater

TARGET_PHRASE = "I am capable of doing anything I put my mind to."

def repeat_until_correct():
    print(f"✨ Type the following affirmation exactly:\n➡️  {TARGET_PHRASE}")
    
    while True:
        attempt = input("> ")
        if attempt == TARGET_PHRASE:
            break
        print("❗ That wasn't quite right. Try again.")

    print("✅ Affirmation accepted! Keep believing in yourself.")

if __name__ == '__main__':
    repeat_until_correct()
