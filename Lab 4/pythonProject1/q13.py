# 0. Write a Java program to enter n elements in an array and find smallest number among
# them.
def min_count():
    n=int(input("Enter number of elements: "))
    array_one=[]
    for i in range (n):
        n=int(input(f"Enter element {i+1}: "))
        array_one.append(n)
    smol=min(array_one)
    return smol

print(f"Samllest Value: {min_count()}")
