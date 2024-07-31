# 13. Write a Java program for following grading system.
# Note: Percentage>=90% : Grade A
# Percentage>=80% : Grade B
# Percentage>=70% : Grade C
# Percentage>=60% : Grade D
# Percentage>=40% : Grade E
# # Percentage<40% : Grade F

# Function to determine grade based on percentage
def determine_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"

# Input from the user
percentage = float(input("Enter the percentage: "))

# Determine the grade
grade = determine_grade(percentage)

# Display the result
print(f"The grade for {percentage}% is: {grade}")
