#7 WAP which makes use of function to display all such numbers which are divisible by 7 but are not a multiple of 5, between
# 1000 to 2000
def num_lis():
    num_list=[]
    for num in range(1000,2001):
        if(num%7==0 and num%5!=0):
            num_list.append(num)
    return num_list

num=num_lis()
print("Numbers divisible by 7 but not a multiple of 5 between 1000 and 2000 are:")
print(num)