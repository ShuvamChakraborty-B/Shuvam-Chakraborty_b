# 11. Print the pattern upto N lines:
# 1 2
# 4 3
#
# 1 2 3
# 8 9 4
# 7 6 5
#
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7

def print_spiral_pattern(N):
    if N <= 0:
        print("N should be a positive integer.")
        return

    # Initialize an N x N matrix
    matrix = [[0] * N for _ in range(N)]

    # Define the boundaries of the spiral
    top, bottom = 0, N - 1
    left, right = 0, N - 1
    num = 1

    while top <= bottom and left <= right:
        # Fill the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Fill the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    # Print the matrix
    for row in matrix:
        print(' '.join(map(str, row)))

# Get user input for N
N = int(input("Enter the number of lines (N): "))

# Print the spiral pattern
print_spiral_pattern(N)
