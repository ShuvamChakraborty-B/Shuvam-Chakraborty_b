# Reverse the elements in an array of integers without using a second array
def reverse_array(arr):
    return arr[::-1]


def main():
    # Read the array from the user
    user_input = input("Enter integers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    # Reverse the array using slicing
    reversed_arr = reverse_array(arr)

    # Print the reversed array
    print("Reversed array:", reversed_arr)


# Call the main function
main()
