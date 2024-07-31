# 9. Convert Decimal number to Binary
def conversion(n):
    if n==0:
        return 0
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n=n//2
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_number =conversion(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")