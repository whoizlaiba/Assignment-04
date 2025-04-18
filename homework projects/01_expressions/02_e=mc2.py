# Question 2: Energy Calculation (E = mc^2)

def calculate_energy():
    c = 299_792_458  # speed of light in m/s
    mass = float(input("Enter mass in kilograms: "))
    energy = mass * (c ** 2)
    print(f"Using E = mc^2")
    print(f"Mass: {mass} kg")
    print(f"Speed of Light: {c} m/s")
    print(f"Energy: {energy} joules")

if __name__ == '__main__':
    calculate_energy()
