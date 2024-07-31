#Write a Java program to change temperature from Fahrenheit to Celsius.
def f_to_c(f):
    return (f- 32) * 5/9


f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{f}°F is equal to {c:.2f}°C")