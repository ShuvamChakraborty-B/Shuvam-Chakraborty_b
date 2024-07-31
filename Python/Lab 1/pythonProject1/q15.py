# 6. Write a Java program to find area and perimeter of a circle.

import math


def calculate_area(radius):
    return math.pi * radius ** 2


def calculate_perimeter(radius):
    return 2 * math.pi * radius


radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)
perimeter = calculate_perimeter(radius)

print(f"The area of the circle is: {area:.2f}")  # format the output to two decimal places.
print(f"The perimeter (circumference) of the circle is: {perimeter:.2f}")
