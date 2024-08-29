def get_matrix_from_user():
    """Function to get a matrix from user input."""
    rows = int(input("Enter the number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter the elements of row {i + 1} separated by spaces: ").split()))
        matrix.append(row)

    return matrix


def is_sparse_matrix(matrix):
    """Function to check if a given matrix is sparse."""
    total_elements = len(matrix) * len(matrix[0])  # Total number of elements in the matrix
    zero_count = sum(row.count(0) for row in matrix)  # Count the number of zero elements

    # A matrix is sparse if the number of zero elements is greater than half the total elements
    return zero_count > (total_elements / 2)


def main():
    # Get the matrix from user input
    matrix = get_matrix_from_user()

    # Check if the matrix is sparse
    if is_sparse_matrix(matrix):
        print("The given matrix is a sparse matrix.")
    else:
        print("The given matrix is not a sparse matrix.")



main()
