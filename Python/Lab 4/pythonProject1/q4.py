# 4. Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
def word_play():
    inp=input("Enter a string:")
    inp1=inp.split()
    remove_duplicate=list(set(inp1) )#set removes duplicates
    remove_duplicate.sort()
    final_result=' '.join(remove_duplicate)
    print(final_result)

word_play()