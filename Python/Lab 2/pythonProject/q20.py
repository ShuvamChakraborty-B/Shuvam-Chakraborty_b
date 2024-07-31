# 8. Write a Java program to print all multiple of 10 between a given interval.
def print_multiples_of_10(start, end):
    # Find the first multiple of 10 within the interval
    if start % 10 != 0:
        start = (start // 10 + 1) * 10

    # Print multiples of 10 within the interval
    for num in range(start, end + 1, 10):
        print(num)

    # Input from the user

start_interval = int(input("Enter the start of the interval: "))
end_interval = int(input("Enter the end of the interval: "))

    # Validate the input
if start_interval > end_interval:
        print("The start of the interval must be less than or equal to the end.")
else:
        # Print multiples of 10 within the specified interval
        print(f"Multiples of 10 between {start_interval} and {end_interval}:")
        print_multiples_of_10(start_interval, end_interval)
