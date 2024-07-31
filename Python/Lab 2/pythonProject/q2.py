#2. To solve the quadratic equation.
def calculate_roots(a,b,c):
    discriminant=b**2-4*a*c

    if discriminant>0:
        root1=(-b + discriminant**0.5)/(2*a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return(root1,root2)
    elif discriminant==0:
        root=(-b)/(2*a)
        return (root,)
    else:
        return "No real roots"


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = calculate_roots(a, b, c)

if isinstance(roots, tuple):  # Check if roots is a tuple
    if len(roots) == 1:  # Single real root
        print(f"The equation has one real root: {roots[0]}")
    else:  # Two distinct real roots
        print(f"The equation has two real roots: {roots[0]} and {roots[1]}")
else:  # No real roots
    print(roots)