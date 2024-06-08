#Write a Python class named Rectangle constructed by a length and
#width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Get input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create a Rectangle object with user input
rectangle = Rectangle(length, width)

# Compute the area and print it
area = rectangle.area()
print("Area of the rectangle:", area)
