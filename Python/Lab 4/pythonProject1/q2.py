# 2.	Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def strn_sort():
    inpp=input("Enter comma-seperated sequence: ")
    words=inpp.split(',')
    words.sort()
    #print(words)
    sorted_words=','.join(words) #converting the list into comma seperated string
    print(sorted_words)
strn_sort()

