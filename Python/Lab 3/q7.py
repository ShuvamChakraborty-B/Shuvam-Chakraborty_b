# 7. Write a program to compute sin x for given x. The user should supply x and a positive integer
# n. We compute the sine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........  (Taylor series)
# import math
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def calculate_sin(x,n):
    sine=0.0
    for i in range(n):
        sign=(-1)**i #alternating sign as necessary
        term=(x**(2*i+1))/factorial(2*i+1)
        sine+=sign*term
    return sine

x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n(terms): "))

if n <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    result = calculate_sin(x, n)
    print(f"The computed value of sin({x}) using {n} terms is: {result}")

# print(math.sin(x))
