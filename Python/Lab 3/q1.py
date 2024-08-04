#1. Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.
def check_season(month):
    month=month.lower() ## Convert month to lowercase to handle case-insensitive input
    if month in ['december','january','february']:
        return "Winter"
    elif month in ['march','april','may']:
        return "Spring"
    elif month in ['june','july','august']:
        return "Summer"
    elif month in ['september','october','november']:
        return "Autumn"
    else:
        return"Invalid Month"



month=input("Enter the required month: ")
print(f"The season in {month.capitalize()} is {check_season(month)}")
