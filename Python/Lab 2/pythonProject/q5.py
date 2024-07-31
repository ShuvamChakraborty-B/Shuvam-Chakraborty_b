import math

# a) sin of 60 degrees
angle_60_degrees = math.radians(60)
sin_60 = math.sin(angle_60_degrees)

# b) cos of pi
cos_pi = math.cos(math.pi)

# c) sin(0.8660254037844386)
sin_value = math.sin(0.8660254037844386)

# d) tan of 90 degrees (handle the undefined case)
angle_90_degrees = math.radians(90)
try:
    tan_90 = math.tan(angle_90_degrees)
except ValueError as e:
    tan_90 = "undefined (approaches infinity)"

print(f"a) sin(60 degrees) = {sin_60}")
print(f"b) cos(pi) = {cos_pi}")
print(f"c) sin(0.8660254037844386) = {sin_value}")
print(f"d) tan(90 degrees) = {tan_90}")
