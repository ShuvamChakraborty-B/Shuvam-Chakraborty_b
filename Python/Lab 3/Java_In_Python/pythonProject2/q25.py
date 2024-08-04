def print_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (i - 1), end="")

        # Print the first number
        print(i, end="")

        if i != n:
            # Print spaces between the two numbers
            print(" " * (2 * (n - i) - 1), end="")

            # Print the second number
            print(i)
        else:
            # Move to the next line after the last number in the last row
            print()


# Get user input for the number of lines
n = int(input("Enter the number of lines (N): "))

# Print the pattern
print_pattern(n)
