import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area
# Test
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")


def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
# Test
perimeter = calculate_perimeter(radius)
print(f"The perimeter of the circle with radius {radius} is: {perimeter:.2f}")
    