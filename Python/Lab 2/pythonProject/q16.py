# 1. Write a Java program to check whether a number is Buzz or not.
def is_buzz_number(num):
    # Check if the number is divisible by 7 or ends with 7
    if num % 7 == 0 or str(num).endswith('7'):
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number: "))
if is_buzz_number(number):
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is not a Buzz number.")
