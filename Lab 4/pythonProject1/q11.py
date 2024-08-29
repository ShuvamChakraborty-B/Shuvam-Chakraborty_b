#diagonal addition
def sum_of_diagonals(matrix):
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]

    return primary_diagonal_sum, secondary_diagonal_sum


def main():
    # Read the size of the matrix
    n = int(input("Enter the size of the matrix (n x n): "))

    # Initialize the matrix
    matrix = []

    # Read the matrix elements from the user
    print("Enter the matrix elements row by row:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Error: The number of elements in each row must be equal to the size of the matrix.")
            return
        matrix.append(row)
    print(matrix)

    # Calculate the sum of diagonals
    primary_diagonal_sum, secondary_diagonal_sum = sum_of_diagonals(matrix)

    # Print the results
    print("Sum of the primary diagonal:", primary_diagonal_sum)
    print("Sum of the secondary diagonal:", secondary_diagonal_sum)


# Call the main function
main()
