# 8. Write a function to calculate the power of a number using recursion
def power_exponent(num,pow):
    if(pow==0):
        return 1
    else:
        return num * power_exponent(num,pow-1)


base=float(input("Enter the base: "))
power=float(input("Enter the power: "))

result=power_exponent(base,power)
print(f"{base}^{power}={result}")