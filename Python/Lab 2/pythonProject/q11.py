# 11. Write a program in Python to find the sum of digits of a number.
def sum_of_digits(num):
    summ = 0
    temp = num
    while temp > 0:
        digits = temp % 10
        summ += digits
        temp = temp // 10
    return summ


number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}")
