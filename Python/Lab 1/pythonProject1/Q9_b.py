#WAP a program in python to check whether a number is an Armstrong number or not
# o='omygod'
# for i in o:
#     print(i)
def Armstrong(num):
    np=str(num)
    length=len(np)
    sum_sum=sum(int(digit)**length for digit in np)
    return num==sum_sum

a=int(input("Enter a number: "))
if Armstrong(a):
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")