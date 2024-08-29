# 1.The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# I. Sort the list and find the min and max age
# II. Add the min age and the max age again to the list
# III. Find the median age (one middle item or two middle items divided by two)
# IV. Find the average age (sum of all items divided by their number )
# V. Find the range of the ages (max minus min)
# VI. Compare the value of (min - average) and (max - average), use _abs()_ method
def analyze_ages(ages):
    # I. Sort the list and find the min and max age
    sorted_ages = sorted(ages)
    min_age = min(sorted_ages)
    max_age = max(sorted_ages)

    print("Sorted ages:", sorted_ages)
    print("Min age:", min_age)
    print("Max age:", max_age)

    # II. Add the min age and the max age again to the list
    updated_ages = sorted_ages + [min_age, max_age]

    print("Updated ages:", updated_ages)

    # III. Find the median age
    n = len(updated_ages)
    if n % 2 == 1:
        median_age = updated_ages[n // 2]
    else:
        median_age = (updated_ages[n // 2 - 1] + updated_ages[n // 2]) / 2

    print("Median age:", median_age)

    # IV. Find the average age
    average_age = sum(updated_ages) / len(updated_ages)

    print("Average age:", average_age)

    # V. Find the range of the ages
    age_range = max_age - min_age

    print("Range of ages:", age_range)

    # VI. Compare the value of (min - average) and (max - average), use abs() method
    min_diff = abs(min_age - average_age)
    max_diff = abs(max_age - average_age)

    print("Absolute difference between min and average:", min_diff)
    print("Absolute difference between max and average:", max_diff)


# List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Analyze the list of ages
analyze_ages(ages)
