# Question 5: Triangle Perimeter

def calculate_perimeter():
    print("== Question 5: Triangle Perimeter ==")
    side_a = float(input("Length of side A: "))
    side_b = float(input("Length of side B: "))
    side_c = float(input("Length of side C: "))
    perimeter = side_a + side_b + side_c
    print(f"The triangle's perimeter is: {perimeter}")

if __name__ == '__main__':
    calculate_perimeter()
