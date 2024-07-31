# 11. Write a Java program to convert miles to kilometers.
# Function to convert miles to kilometers
def miles_to_kilometers(miles):
    return miles * 1.60934


# Input from the user
miles = float(input("Enter the distance in miles: "))

# Convert miles to kilometers
kilometers = miles_to_kilometers(miles)

# Display the result
print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
