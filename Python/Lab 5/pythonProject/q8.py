season_map = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'
}


# Function to get the season based on month number
def get_season(month_number):
    return season_map.get(month_number, "Invalid")


# Get user input

month = int(input("Enter the month number (1-12): "))
season = get_season(month)
print(f"The season for month {month} is {season}.")
