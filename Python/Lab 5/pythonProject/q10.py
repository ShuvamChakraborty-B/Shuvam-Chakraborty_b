def get_matrix_from_user():
    """Function to get a matrix from user input."""
    rows = int(input("Enter the number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter the elements of row {i + 1} separated by spaces: ").split()))
        matrix.append(row)

    return matrix


def transpose_matrix(matrix):
    """Function to transpose a given matrix."""
    # Transpose the matrix using list comprehension
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed


def print_matrix(matrix):
    """Function to print the matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    # Get the matrix from user input
    matrix = get_matrix_from_user()

    # Compute the transpose of the matrix
    transposed = transpose_matrix(matrix)

    # Print the original matrix
    print("\nOriginal matrix:")
    print_matrix(matrix)

    # Print the transposed matrix
    print("\nTransposed matrix:")
    print_matrix(transposed)



main()
