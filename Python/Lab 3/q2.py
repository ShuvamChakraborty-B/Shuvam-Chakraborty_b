# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,x2,y1,y2):
    if x1==x2:
        return "Undefined Slope as it is a vertical line!"
    else:
        return (y2-y1)/(x2-x1)

x1,y1=map(float,input("Enter the values for x1 and y1: ").split())
# The map() function applies the float function to each element in the list produced by split().
x2,y2=map(float,input("Enter the values for x2 and y2: ").split())
slope=calculate_slope(x1, x2, y1, y2)
print(f"The slope of the line through points ({x1}, {y1}) and ({x2}, {y2}) is {slope}.")