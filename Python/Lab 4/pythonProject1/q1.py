# Write a program to enter a string. Calculate the length of the string. Find the substring country.
# Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

def string_test():
    input_string=input("Enter the string: ")
    #calculate length
    length_string=len(input_string)
    print(f"The length of the string is: {length_string}")
    #find substring
    if "country" in input_string:
        print("Substring 'country' is present in the string. ")
    else:
        print("Substring 'country' is not present in the string. ")

    #occurences
    #remove puncutation
    strn=input_string.lower().replace('.','').split()
    word_count={}
    for word in strn:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    print("Number of occurences: ")
    for words,count in word_count.items(): #.items() is necessary for key and value pairs
        print(f"{words}:{count}")

string_test()

