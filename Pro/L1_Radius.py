class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def is_square(self):
        if self.width != self.height:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def __repr__(self):
        return f"ширина = {self.width}, высота = {self.height}"


rd = Rectangle(30, 5)
print(rd)
print('Площадь: ', rd.area())
print('Периметр: ', rd.perimeter())
print(rd.is_square())
rd.resize(56, 20)
print(rd)
print('Площадь: ', rd.area())
print('Периметр: ', rd.perimeter())
