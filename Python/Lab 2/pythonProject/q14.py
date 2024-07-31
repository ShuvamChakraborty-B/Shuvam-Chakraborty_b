# 14. Print the series upto N terms: 1,2,6,24,120,720 …
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n * facto(n-1)

def facto_series(n):
    for i in range(1,n+1):
        if i < n:
            print(f"{facto(i)}, ", end="")
        else:
            print(f"{facto(i)}")

N = int(input("Enter the number of terms: "))
print(f"The first {N} terms of the factorial series are:")
facto_series(N)