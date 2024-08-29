# Write a Java program to find the sum of even numbers in an integer array
def addition(a):
    sum=0
    for num in a:
        if num%2==0:
            sum+=num
    return sum
user_input=list(map(int,input("Enter integers seperated by spaces: ").split()))
sum=addition(user_input)
print("Sum=",sum)