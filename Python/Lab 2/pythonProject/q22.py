# 12. Write a Java program to count the number of digits of an integer.
def count_digits(number):
    # Convert the number to its absolute value to handle negative numbers
    number = abs(number)

    # If the number is zero, it has one digit
    if number == 0:
        return 1

    # Count digits
    digit_count = 0
    while number > 0:
        number //= 10
        digit_count += 1

    return digit_count


# Input from the user

num = int(input("Enter an integer: "))
    # Count and print the number of digits
print(f"The number of digits in {num} is: {count_digits(num)}")

