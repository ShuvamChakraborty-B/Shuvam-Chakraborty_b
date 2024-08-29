# Given sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# I. Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)

# III. Insert multiple IT companies at once to the set it_companies
new_companies = {'Netflix', 'Adobe', 'Slack'}
it_companies.update(new_companies)
print("Updated it_companies with multiple companies:", it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')  # Example removal
print("Updated it_companies after removing one company:", it_companies)

# # V. Difference between remove and discard
# # Example to demonstrate remove and discard
# it_companies.discard('NonExistentCompany')  # Does nothing if the element does not exist
# try:
#     it_companies.remove('NonExistentCompany')  # Raises KeyError if the element does not exist
# except KeyError:
#     print("Element not found while using remove.")


join_A_B = A | B
print("Join A and B:", join_A_B)

# II. Find A intersection B
intersection_A_B = A & B
print("Intersection of A and B:", intersection_A_B)

# III. Is A a subset of B
is_A_subset_B = A.issubset(B)
print("Is A a subset of B:", is_A_subset_B)

# IV. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_disjoint)

# V. Join A with B and B with A
join_A_with_B = A | B
join_B_with_A = B | A
print("Join A with B:", join_A_with_B)
print("Join B with A:", join_B_with_A)

# VI. Symmetric difference between A and B
symmetric_difference_A_B = A ^ B
print("Symmetric difference between A and B:", symmetric_difference_A_B)

# VII. Delete the sets completely
del A
del B