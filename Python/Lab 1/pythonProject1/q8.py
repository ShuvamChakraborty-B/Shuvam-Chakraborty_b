# Write a program to check whether a number is a pallindrome or not
def pallindrome_check(num):
    nu=str(num)
    if nu==nu[::-1]:
        return  True
    else:
        return False

a=int(input("Enter a number to check whether it is a pallindrome: "))
if pallindrome_check(a):
    print(f"{a} is a pallindrome ")
else:
    print(f"{a} is not a pallindrome ")

