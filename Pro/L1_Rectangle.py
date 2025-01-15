# Создаём класс Прямоугольника
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # Ширина
        self.height = height  # Высота

    # Вычисляем площадь
    def area(self):
        return self.width * self.height

    # Вычисляем периметр
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Определяем, квадрат или прямоугольник
    def is_square(self):
        if self.width != self.height:
            return True  # Прямоугольник
        else:
            return False  # Квадрат

    # Изменяем размер прямоугольника
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    # Для вывода ширины и высоты
    def __str__(self):
        return f"ширина = {self.width}, высота = {self.height}"


rd = Rectangle(30, 5)  # Назначаем ширину и высоту
print(rd)  # Выводим ширину и высоту
print('Площадь: ', rd.area())  # Выводим площадь
print('Периметр: ', rd.perimeter())  # Выводим периметр
print(rd.is_square())  # Выводим его точность
rd.resize(56, 20)  # Меняем размер
# И снова выводим площадь
print(rd) # Выводим ширину и высоту
print('Площадь: ', rd.area()) # Выводим площадь
print('Периметр: ', rd.perimeter()) # Выводим периметр
print(rd.is_square())  # Выводим его точность
