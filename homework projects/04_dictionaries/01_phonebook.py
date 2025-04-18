# Question 2: Simple Phonebook

def create_phonebook():
    directory = {}
    while True:
        name = input("Enter contact name (or press Enter to stop): ").strip()
        if not name:
            break
        number = input(f"Enter phone number for {name}: ")
        directory[name] = number
    return directory

def display_contacts(phonebook):
    print("\n📇 Phonebook Entries:")
    for person in phonebook:
        print(f"{person}: {phonebook[person]}")

def search_contact(phonebook):
    name = input("\n🔍 Search by name: ")
    if name in phonebook:
        print(f"✅ Found: {name} → {phonebook[name]}")
    else:
        print(f"❌ {name} is not in the phonebook.")

if __name__ == '__main__':
    book = create_phonebook()
    display_contacts(book)
    search_contact(book)
