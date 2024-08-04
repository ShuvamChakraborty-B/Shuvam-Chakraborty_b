def get_8_segment_digit(digit):
    # Define the 8-segment representation for each digit
    segments = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"],
    }
    return segments[digit]


def print_8_segment_display(number):
    # Convert number to string to iterate through each digit
    number_str = str(number)

    # Initialize lists to hold each row of the display
    rows = ["", "", ""]

    # Build the display rows by concatenating each digit's segments
    for digit in number_str:
        segments = get_8_segment_digit(digit)
        for i in range(3):
            rows[i] += segments[i]

            # Print each row
    for row in rows:
        print(row)


# Input from the user
number = input("Enter a number: ")
print_8_segment_display(number)
