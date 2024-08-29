# 5. Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
def counting():
    inp_strn=input("Enter the string: ")
    letter_count=0
    digit_count=0
    for words in inp_strn:
        if words.isalpha():
            letter_count+=1
        if words.isdigit():
            digit_count+=1

    print(f"LETTERS {letter_count}")
    print(f"DIGITS {digit_count}")

counting()