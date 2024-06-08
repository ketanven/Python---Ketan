#Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
area = circle.area()
perimeter = circle.perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
