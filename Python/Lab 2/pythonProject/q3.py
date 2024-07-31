#3.Find GCD of two numbers
def calculate_GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_GCD(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")