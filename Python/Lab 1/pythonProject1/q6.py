def generate_prime(n):
    prime_series = [] #2 1 3 2 5 3 7 4 11 5 13 6 17 7 19 8 23 9 29 10
    num = 2
    while (len(prime_series)) < n :
        if is_prime(num):
            prime_series.append(num)
        num += 1

    return prime_series


def is_prime(n):
    # If the loop completes without finding any divisors, it means num is not divisible by any number other than 1 and itself, so it is a
    # prime number.The function returns True.
    if n <= 1:
        return False
    else:
        for i in range(2,
                       int(n ** 0.5) + 1):  # When checking if a number is prime, you only need to test for factors up to its square root.
            # If a number has a factor larger than its square root, it must also have a corresponding factor smaller than the square root.
            if n % i == 0:
                return False
        return True


n = int(input("Enter the required term: "))
k=generate_prime(n)
print(k)
