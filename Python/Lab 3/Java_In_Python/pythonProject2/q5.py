# 5. Write a Java program to find the range of a 1D array.
def find_range(arr):
    # Ensure the array is not empty
    if len(arr) == 0:
        return None

    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the range
    range_val = max_val - min_val

    return range_val

# Example usage
arr = [5, 10, 15, 20, 25, 30]

print("Array:", arr)
range_val = find_range(arr)
if range_val is not None:
    print("Range of the array:", range_val)
else:
    print("Array is empty, no range to calculate.")
