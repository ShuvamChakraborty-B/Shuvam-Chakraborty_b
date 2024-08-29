# Write a Java program which counts the non-zero elements in an integer array.
def count_non_zero_elements(array):
    """Function to count the number of non-zero elements in an array."""
    non_zero_count = 0

    for num in array:
        if num != 0:
            non_zero_count += 1

    return non_zero_count


def main():
    # Read the array from user input
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Count the non-zero elements in the array
    non_zero_count = count_non_zero_elements(array)

    # Print the result
    print("Number of non-zero elements in the array:", non_zero_count)



main()
