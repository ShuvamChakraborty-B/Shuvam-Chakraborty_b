# 11. Write a Java program to find LCM of two Numbers
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# Input from the user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Validate the input
if num1 <= 0 or num2 <= 0:
    print("Please enter positive integers.")
else:
    # Calculate the LCM
    result = lcm(num1, num2)
    # Print the result
    print(f"The LCM of {num1} and {num2} is: {result}")
