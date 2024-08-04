# 6. Compute the sum up to n terms in the series
# 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.
def computation(terms):
  #  b=float(terms)
    n=0.0
    for i in range (1,terms+1):
        if i%2==0:
            n-=1/i
        else:
            n+=1/(i)
    return n

inp=int(input("Enter the number of terms: ")) #cant use float due to range function
print(f"The value for {inp} terms is {computation(inp)}")