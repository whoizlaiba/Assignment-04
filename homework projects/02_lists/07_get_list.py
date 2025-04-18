# Question 7: Build a List from User Input

def collect_user_input():
    items = []
    entry = input("Add a value to your list: ")
    while entry:
        items.append(entry)
        entry = input("Add another value (or press Enter to finish): ")
    return items

def main():
    user_list = collect_user_input()
    print("Your final list:", user_list)

if __name__ == '__main__':
    main()
