def find_second_highest(array):
    """Function to find the second highest element in an array."""
    # Remove duplicates by converting the array to a set, then back to a list
    unique_elements = list(set(array))

    # Check if there are at least two unique elements
    if len(unique_elements) < 2:
        return None  # No second highest element exists

    # Sort the unique elements in descending order
    unique_elements.sort(reverse=True)

    # Return the second highest element
    return unique_elements[1]


def main():
    # Read the array from user input
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Find the second highest element
    second_highest = find_second_highest(array)

    # Print the result
    if second_highest is None:
        print("There is no second highest element in the array.")
    else:
        print("The second highest element in the array is:", second_highest)


main()
