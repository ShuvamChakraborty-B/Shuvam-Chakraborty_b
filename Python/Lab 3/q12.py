# 12. Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

def print_pattern(n):
    for i in range(1,n+1):
        row=[i,i**0,i**1,i**2,i**3]
        print(" ".join(map(str,row)))


i=int(input("Enter the term: "))
print_pattern(i)