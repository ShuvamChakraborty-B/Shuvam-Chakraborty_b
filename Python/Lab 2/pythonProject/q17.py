# 2. Write a Java program to calculate factorial of 12.
# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 12
number = 12
result = factorial(number)

# Print the result
print(f"The factorial of {number} is: {result}")

