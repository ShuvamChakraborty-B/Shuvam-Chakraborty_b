# . Write Java program to find the sum of all odd numbers in a 2D array.
def sum_of_odd_numbers_2D(matrix):
    total_sum = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:  # Check if the number is odd
                total_sum += num
    return total_sum


def main():
    # Read the number of rows
    rows = int(input("Enter the number of rows: "))

    # Read the number of columns
    cols = int(input("Enter the number of columns: "))

    # Initialize the 2D array
    matrix = []

    # Read the 2D array elements from the user
    print(f"Enter the elements of the {rows}x{cols} matrix row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            try:
                num = int(input(f"Element ({i + 1},{j + 1}): "))
                row.append(num)
            except ValueError:
                print("Please enter a valid integer.")
                return
        matrix.append(row)

    # Calculate the sum of odd numbers in the 2D array
    sum_odds = sum_of_odd_numbers_2D(matrix)

    # Print the result
    print("Sum of all odd numbers in the 2D array:", sum_odds)


# Call the main function
main()
