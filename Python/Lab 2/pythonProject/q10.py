# # 10. Write a program in Python to check if a number is Krishnamurthy number.
# A Krishnamurthy number (also known as a strong number or a Peterson number) is a number whose sum of the factorials of its digits is equal to the number itself. For example, 145 is a Krishnamurthy number because
# 1
# !
# +
# 4
# !
# +
# 5
# !
# =
# 1
# +
# 24
# +
# 120
# =
# 145
# 1!+4!+5!=1+24+120=145.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def krishnamurti_check(num):
    sum_of_factorials=0
    temp=num
    while temp>0:
        digit=temp%10
        sum_of_factorials+=factorial(digit)
        temp=temp//10 #taking quotient
    return sum_of_factorials==num

num=int(input("Enter a number: "))
if krishnamurti_check(num):
    print(f"{num} is a Krishnamurti Number")
else:
    print(f"{num} is not a Krishnamurti Number")
