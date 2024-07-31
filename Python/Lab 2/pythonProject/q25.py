# 19. Write a Java program to generate all combination of 1, 2, or 3 using loop
def generate_combinations():
    numbers = [1, 2, 3]

    # Generate combinations of length 1
    print("Combinations of length 1:")
    for num1 in numbers:
        print(num1)

    # Generate combinations of length 2
    print("\nCombinations of length 2:")
    for num1 in numbers:
        for num2 in numbers:
            print(num1, num2)

    # Generate combinations of length 3
    print("\nCombinations of length 3:")
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                print(num1, num2, num3)


# Call the function to generate and print combinations
generate_combinations()
