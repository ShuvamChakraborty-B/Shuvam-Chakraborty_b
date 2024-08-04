# 4. Declare a function named print_list. It takes a list as a parameter and it prints out each
# element of the list.
def print_list(listy):
    for items in listy:
        print(items)

inp=(input("Enter values for a list: ").split())
print_list(inp)