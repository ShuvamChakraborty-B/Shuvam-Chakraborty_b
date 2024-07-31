#1. To find the sum of square root of any three numbers.
def root(a,b,c):
     a1=a**0.5
     b1=b**0.5
     c1=c**0.5
     return a1+b1+c1

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
print(f"The sum of the square roots of {num1}, {num2}, {num3} is {root(num1,num2,num3)}")