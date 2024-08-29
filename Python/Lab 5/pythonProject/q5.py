# Create an empty dictionary
dog = {}

# Prompt user to input values for each attribute
dog['name'] = input("Enter the dog's name: ")
dog['color'] = input("Enter the dog's color: ")
dog['breed'] = input("Enter the dog's breed: ")
dog['legs'] = int(input("Enter the number of legs the dog has: "))
dog['age'] = int(input("Enter the dog's age: "))

# Print the dictionary to verify the attributes
print("Dog dictionary:", dog)
