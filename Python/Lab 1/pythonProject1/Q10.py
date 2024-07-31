# #WAP to print fibonacci series upto nth term
def fib_series(n):
    fib_seriess=[]
    a=0
    b=1
    while (len(fib_seriess))<n: #fib_series=0, initial value
        fib_seriess.append(a)
        c=a+b
        a=b
        b=c
    return fib_seriess

a=int(input("Enter total terms: "))
print(fib_series(a))


# b='10'
# a=len(b)
# # while a<int(b):
# #     print(a)
# #     a=a+1
# #     # b=b+1
# o=[]
# print(len(o))
