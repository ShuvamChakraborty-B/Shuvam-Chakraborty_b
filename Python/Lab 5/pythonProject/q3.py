# Define the tuples
fruits = ('apple', 'banana', 'cherry', 'date', 'fig')
vegetables = ('carrot', 'broccoli', 'asparagus', 'spinach', 'potato')
animal_products = ('milk', 'cheese', 'butter', 'yogurt', 'eggs')

# I. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)

# II. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
# Find the middle index
n = len(food_stuff_lt)
if n % 2 == 1:

    middle_slice = food_stuff_lt[n // 2]
else:
    middle_slice = food_stuff_lt[n // 2 - 1 : n // 2 + 1]

print("Middle item(s):", middle_slice)

# IV. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)


del food_stuff_tp
