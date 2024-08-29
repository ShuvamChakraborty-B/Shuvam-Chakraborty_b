def sum_of_odd_numbers_2d(array_2d):
    """Function to find the sum of all odd numbers in a 2D array."""
    total_sum = 0
    for row in array_2d:
        for num in row:
            if num % 2 != 0:  # Check if the number is odd
                total_sum += num
    return total_sum


def get_2d_array_from_user():
    """Function to get a 2D array from user input."""
    rows = int(input("Enter the number of rows: "))
    array_2d = []

    for i in range(rows):
        # Prompt user to enter the elements of the row separated by spaces
        row = list(map(int, input(f"Enter the elements of row {i + 1} separated by spaces: ").split()))
        array_2d.append(row)

    return array_2d


def main():
    # Get 2D array from the user
    array_2d = get_2d_array_from_user()

    # Calculate the sum of all odd numbers
    result = sum_of_odd_numbers_2d(array_2d)

    # Print the result
    print("Sum of all odd numbers:", result)


if __name__ == "__main__":
    main()
