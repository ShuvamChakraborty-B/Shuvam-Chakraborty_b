# 9. Write a Java program to find maximum of three numbers.
# Function to find the maximum of three numbers
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum number
maximum = find_maximum(num1, num2, num3)

# Print the result
print(f"The maximum of the three numbers is: {maximum}")
