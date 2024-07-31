# 17. Write a Java program to find median of a set of numbers.
def find_median(numbers):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Calculate the length of the list
    n = len(sorted_numbers)

    # Check if the number of elements is odd or even
    if n % 2 == 1:
        # Odd number of elements: return the middle element
        return sorted_numbers[n // 2]
    else:
        # Even number of elements: return the average of the two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


# Input from the user

    # Read numbers from the user
user_input = input("Enter a set of numbers separated by spaces: ")
    # Convert input string to a list of numbers
numbers = list(map(float, user_input.split()))

    # Check if list is empty
if not numbers:
        print("No numbers provided.")
else:
        # Find and print the median
    median = find_median(numbers)
    print(f"The median is: {median}")


