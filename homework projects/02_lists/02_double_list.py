# Question 2: Double Each Element in List

def double_each_item(input_list):
    result = []
    for item in input_list:
        result.append(item * 2)
    print(f"Doubled list: {result}")

if __name__ == '__main__':
    numbers_to_double = [1, 2, 3, 4, 5]
    double_each_item(numbers_to_double)
