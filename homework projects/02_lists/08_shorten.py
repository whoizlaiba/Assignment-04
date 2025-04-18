# Question 8: Shorten List to Max Length

MAX_ITEMS = 3

def trim_list_down(lst):
    while len(lst) >= MAX_ITEMS:
        removed = lst.pop()
        print("Removed:", removed)

def collect_items():
    result = []
    element = input("Enter an item (blank to stop): ")
    while element != "":
        result.append(element)
        element = input("Enter an item (blank to stop): ")
    return result

def main():
    data = collect_items()
    trim_list_down(data)

if __name__ == '__main__':
    main()
