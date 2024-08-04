# 20. Write a Java program to read two integer values m and n and to decide and print
# whether m is multiple of n.
def multiple_check(m,n):
    if n==0:
        return "Division by 0 is not allowed"
    else:
        if m%n==0:
            return f"{m} is a multiple of {n}"
        else:
            return f"{m} is not a multiple of {n}"

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
print(multiple_check(m,n))