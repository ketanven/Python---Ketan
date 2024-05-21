# Write a Python program to calculate the area of a parallelogram


def parallelogram_area(base, height):
    return base * height

# Ask the user for input
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

# Calculate the area of the parallelogram and print the result
area = parallelogram_area(base, height)
print("Area of the parallelogram:", area)
