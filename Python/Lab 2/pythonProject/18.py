# 5. Admission to a professional course is subject to the following conditions:
# (a) marks in Mathematics >= 60 (b) marks in Physics >=50
# (c) marks in Chemistry >=40 (d) Total in all 3 subjects >=200
#  (Or)
#  Total in Maths & Physics>=150
# Given the marks in the 3 subjects of n (user input) students, write a program to process
# the applications to list the eligible candidates.
def is_eligible(maths, physics, chemistry):
    # Condition (a), (b), (c), and (d)
    if (maths >= 60 and physics >= 50 and chemistry >= 40 and
        (maths + physics + chemistry) >= 200):
        return True
    # Condition (e)
    elif (maths + physics) >= 150:
        return True
    return False

def process_applications(n):
    eligible_candidates = []

    for i in range(n):
        print(f"\nEnter marks for student {i + 1}:")
        maths = float(input("Mathematics: "))
        physics = float(input("Physics: "))
        chemistry = float(input("Chemistry: "))

        if is_eligible(maths, physics, chemistry):
            eligible_candidates.append(f"Student {i + 1}")

    return eligible_candidates

# Number of students
n = int(input("Enter the number of students: "))
eligible_students = process_applications(n)

# Print eligible students
if eligible_students:
    print("\nEligible candidates:")
    for student in eligible_students:
        print(student)
else:
    print("\nNo eligible candidates.")

