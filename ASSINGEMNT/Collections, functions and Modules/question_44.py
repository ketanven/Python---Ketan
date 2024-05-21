# Write a Python program to convert degree to radian

import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

# Ask the user for input
degrees = float(input("Enter degrees: "))

# Convert degrees to radians and print the result
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians")
