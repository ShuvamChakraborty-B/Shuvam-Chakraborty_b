#2.WAP to swap two numbers
# Function to swap two numbers
def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = swap_numbers(num1, num2)

print(f"After swapping: num1 = {num1}, num2 = {num2}")
