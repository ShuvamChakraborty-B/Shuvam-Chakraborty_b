# 5. Declare a function named reverse_list. It takes an array as a parameter and it returns the
# reverse of the array (use loops).
def reverse_list(arr):
    revers_a=[]
    for i in range(len(arr)-1,-1,-1):
        revers_a.append(arr[i])
    return revers_a


a=(input("Enter values:").split())
revers_a=reverse_list(a)
print(revers_a)