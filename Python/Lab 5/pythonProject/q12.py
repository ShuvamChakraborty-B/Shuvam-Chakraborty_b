def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is a prime number
    if num % 2 == 0:
        return False  # Exclude even numbers greater than 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def count_primes_in_array(array):
    """Function to count the number of prime numbers in an array."""
    prime_count = 0
    for num in array:
        if is_prime(num):
            prime_count += 1
    return prime_count


def main():
    # Read the array from user input
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Count the number of primes in the array
    prime_count = count_primes_in_array(array)

    # Print the result
    print("Number of prime numbers in the array:", prime_count)



main()
