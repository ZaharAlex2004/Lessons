class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width + self.height


rd = Rectangle(30, 5)
print(rd.area())
print(rd.perimeter())
