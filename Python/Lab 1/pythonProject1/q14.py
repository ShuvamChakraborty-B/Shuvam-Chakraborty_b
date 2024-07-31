#Write a Java program to find area and perimeter of a rectangle.
def area(l,b):
    return l*b
def perimeter(l,b):
    return 2*(l+b)

a=float(input("Enter Length: "))
b=float(input("Enter Breadth: "))
print("Area = ", area(a,b))
print("Perimeter= ", perimeter(a,b))
