#WAP a program in python to check whether a number is a perfect number or not
def perfect_number_check(num):
    sum=0
    if num<1:
        return False
    else:
        for i in range(1,num):
            if num%i==0:
                sum=sum+i

    return num==sum

A=int(input("Enter a number: "))
if perfect_number_check(A):
    print(f"{A} is a perfect number")
else:
    print(f"{A} is not a perfect number")