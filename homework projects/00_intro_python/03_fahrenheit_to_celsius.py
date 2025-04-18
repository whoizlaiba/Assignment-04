# Question 3: Convert Fahrenheit to Celsius

def convert_temp():
    print("== Question 3: Fahrenheit to Celsius Converter ==")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == '__main__':
    convert_temp()
