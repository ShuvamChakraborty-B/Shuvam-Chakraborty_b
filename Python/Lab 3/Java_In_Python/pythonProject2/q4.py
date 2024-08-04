# 4. Write a Java program to calculate Sum of two 2-dimensional arrays.
def sum_of_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows = len(matrix1)
    cols = len(matrix1[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate through each element of the matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Example usage
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

result = sum_of_matrices(matrix1, matrix2)
print("\nSum of Matrix 1 and Matrix 2:")
print_matrix(result)
