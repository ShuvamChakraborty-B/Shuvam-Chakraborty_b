#triangles
def bingo_madangles(n):
    if n<=0:
        print("Enter a positive number.")
        return

    for i in range(1,n+1):
        space=" "*(n-i)
        if i==1:
            print(f"{space}.")
        else:
            line='/'+' '*(2*i-3)+ '\\'
            if i==n:
                line='/'+'_'*(2*i-3)+'\\'
            print(f"{space}{line}")

i=int(input("Enter the required value: "))

bingo_madangles(i)

