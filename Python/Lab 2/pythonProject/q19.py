# 7. Write a Java program to calculate the sum of natural numbers up to a certain range.
# Function to calculate the sum of natural numbers up to a certain range
def sum_of_natural_numbers(n):
    return sum(range(1, n + 1))


# Input from the user

range_limit = int(input("Enter the range (positive integer): "))

# Validate the input
if range_limit < 1:
    print("Please enter a positive integer greater than 0.")
else:
    # Calculate the sum of natural numbers up to the specified range
    total_sum = sum_of_natural_numbers(range_limit)
    # Print the result
    print(f"The sum of natural numbers up to {range_limit} is: {total_sum}")
