# Create a student dictionary
student = {
    'first_name': 'Bigby',
    'last_name': 'Wolf',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Fable Town'
}

# I. Get the length of the student dictionary
length_of_dict = len(student)
print("Length of the student dictionary:", length_of_dict)

# II. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# III. Modify the skills values by adding one or two skills
student['skills'].extend(['Django', 'Flask'])
print("Updated skills:", student['skills'])

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# V. Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# VI. Change the dictionary to a list of tuples using items()
items_list = list(student.items())
print("List of tuples (key-value pairs):", items_list)

# VII. Delete one of the items in the dictionary
del student['address']
print("Dictionary after deleting 'address':", student)

# VIII. Delete the dictionary completely
del student

