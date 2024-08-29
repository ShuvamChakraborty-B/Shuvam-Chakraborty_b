# 9.Write a program that accepts a string
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence

def process_string():
    # Input string
    input_string = input("Enter a string: ")

    # Task I: Reverse the string
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)

    # Task II: Check if the string is a palindrome
    is_palindrome = input_string == reversed_string
    print("Is palindrome:", is_palindrome)

    # Task III: Check if the string ends with a specific substring
    substring = input("Enter the substring to check if the string ends with it: ")
    ends_with_substring = input_string.endswith(substring)
    print("Ends with substring:", ends_with_substring)

    # Task IV: Capitalize the first letter of each word
    capitalized_string = input_string.title()
    print("Capitalized string:", capitalized_string)

    # Task V: Check if the string is an anagram of another string
    other_string = input("Enter another string to check if it's an anagram: ")
    is_anagram = sorted(input_string) == sorted(other_string)
    print("Is anagram:", is_anagram)

    # Task VI: Remove vowels from the string
    vowels = "aeiouAEIOU"
    no_vowels_string = ''.join(char for char in input_string if char not in vowels)
    print("String without vowels:", no_vowels_string)

    # Task VII: Find the length of the longest word in a sentence
    sentence = input("Enter a sentence to find the length of the longest word: ")
    words = sentence.split()
    longest_word_length = max(len(word) for word in words) if words else 0
    print("Length of the longest word:", longest_word_length)


# Call the function
process_string()
