#4.WAP to display reverse of a number
def reverse_no(num):
    reverse_n=0
    while num>0:
        digit=num%10
        reverse_n=reverse_n*10+digit
        num=num//10    # # Use floor division to keep num as an integer

    return reverse_n

i=int(input("Enter an integer: "))
j=reverse_no(i)
print(f"The reverse of {i} is {j}")
