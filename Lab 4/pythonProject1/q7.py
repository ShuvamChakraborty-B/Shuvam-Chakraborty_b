def digit_count():
    inp=input("Enter a string: ")
    j=inp.split()
    count=[]
    for words in j:
        if words.isdigit():
            count.append(words)
    print(count)
digit_count()