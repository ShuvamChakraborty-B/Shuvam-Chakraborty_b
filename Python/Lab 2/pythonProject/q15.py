# 15. Write a Python program that prompts the user to enter a base number and an exponent,
# and then calculates the power of the base to the exponent. The program should not use the
# exponentiation operator (**) or the math.pow() function.
def power_v(base,exponent):
    result=1
    for i in range(exponent):
        result=result*base

    return result

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
power_result = power_v(base, exponent)
print(f"{base} to the power of {exponent} is {power_result}")