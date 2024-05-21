# Write a Python program to calculate the area of a trapezoid


def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

# Ask the user for input
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))

# Calculate the area of the trapezoid and print the result
area = trapezoid_area(base1, base2, height)
print("Area of the trapezoid:", area)
