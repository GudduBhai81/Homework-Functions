import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Example usage
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")