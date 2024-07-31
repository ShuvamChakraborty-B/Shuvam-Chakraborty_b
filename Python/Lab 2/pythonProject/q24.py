# 18. Write a program to compute the value of Euler’s number that is used as the base of
# natural logarithms. Use the following formula.
# e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!
import math


def compute_euler_number(n_terms):
    # Initialize e to 1 (which is the first term in the series)
    e = 1.0

    # Sum the series up to n_terms
    for i in range(1, n_terms):
        e += 1 / math.factorial(i)

    return e


# Input from the user
try:
    num_terms = int(input("Enter the number of terms for approximation: "))

    # Validate the input
    if num_terms < 1:
        print("The number of terms must be at least 1.")
    else:
        # Compute Euler's number
        euler_number = compute_euler_number(num_terms)
        # Print the result
        print(f"Approximation of Euler's number (e) using {num_terms} terms is: {euler_number}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
