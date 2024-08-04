# 1. Write a Java program to calculate Sum & Average of an integer array
def calculate_sum_and_average(arr):
    if len(arr) == 0:
        return 0, 0.0  # Handle empty array case

    total_sum = sum(arr)
    average = total_sum / len(arr)
    return total_sum, average


# Get user input for the integer array
array = list(map(int, input("Enter integers separated by spaces: ").split()))

# Calculate sum and average
total_sum, average = calculate_sum_and_average(array)

# Print the results
print(f"Sum: {total_sum}")
print(f"Average: {average}")
