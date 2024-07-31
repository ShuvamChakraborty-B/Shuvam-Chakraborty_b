# WAP in python to find the factors of a given number
def factorization(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


i = int(input("Enter an integer: "))
print(f"The factors of {i} is/are {factorization(i)}")
