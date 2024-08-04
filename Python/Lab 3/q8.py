# 8. Write a program to compute cosine of x. The user should supply x and a positive integer n.
# We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn
# cos x = 1 - x2/2! + x4/4! - x6/6! ....

import math
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def calculate_cosin(x,n):
    sine=0.0
    for i in range(n):
        sign=(-1)**i #alternating sign as necessary
        term=(x**(2*i))/factorial(2*i)
        sine+=sign*term
    return sine

x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n(terms): "))

if n <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    result = calculate_cosin(x, n)
    print(f"The computed value of cosine({x}) using {n} terms is: {result}")

print(math.cos(x))
