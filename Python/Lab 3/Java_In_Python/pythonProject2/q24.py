#pyramid
def print_pyramid_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print decreasing part
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Print increasing part
        for j in range(2, i + 1):
            print(j, end=" ")

        # Move to the next line
        print()


# Get user input for the number of lines
n = int(input("Enter the number of lines (N): "))
print_pyramid_pattern(n)
