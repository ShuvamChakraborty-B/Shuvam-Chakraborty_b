# 3. Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD

def cap():

    lines=[]
    while True:
        try:
            in_strn = input("Enter lines of text and Press Ctrl+D to end!: ")
        except EOFError:
            break
        lines.append(in_strn)
        #print(lines)

    for line in lines:
        print(line.upper())

cap()
