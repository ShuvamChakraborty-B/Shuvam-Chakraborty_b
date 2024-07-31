# 12. Write a program in Python that prompts the user to input a number and prints its
# # multiplication table.
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Prompt the user for input
number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")

# Call the function to print the multiplication table
print_multiplication_table(number)
