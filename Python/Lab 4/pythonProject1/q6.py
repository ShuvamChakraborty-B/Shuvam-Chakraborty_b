# To write a program that checks if a given string is "yes", "YES", or "Yes" and prints "Yes" if it matches any of these variations, otherwise prints "No",
def check_string():
    # Accept a string input from the user
    user_input = input("Enter a string: ")

    # Check if the input matches "yes", "YES", or "Yes"
    if user_input in ("yes", "YES", "Yes"):
        print("Yes")
    else:
        print("No")


# Call the function
check_string()
