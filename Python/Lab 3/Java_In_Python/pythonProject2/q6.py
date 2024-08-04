def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example usage
array = list(map(int, input("Enter integers separated by spaces: ").split()))
search_key = int(input(("Enter the value that needs to be searched: ")))
result = linear_search(array, search_key)
if result != -1:
    print(f"Element found at position: {result + 1}")
else:
    print("Element not found")
