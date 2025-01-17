class rectangle:
    """
    Класс Rectangle используется для вычисления площади,
    периметра и изменения размера прямоугольника. А также
    определения квадрата или прямоугольника.

    Attributes
    ----------
    width - ширина
    height - высота
    """
    def __init__(self, width, height):
        """
        Инициализация класса.
        :self.width = width: ширина
        :self.height = height: высота
        """
        self.width = width  # ширина
        self.height = height  # высота

    def area(self):
        """
        Функция вычисления площади.
        :return: произведение self.width и self.height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Функция вычисления периметра.
        Периметр - сумма длин всех сторон.
        :return: в скобках сумма self.width и self.height и умножние на 2
        """
        return 2 * (self.width + self.height)

    def is_square(self):
        """
        Функция определения квадрата или прямоугольника.
        Если self.width не равен self.height, то это прямоугольник (True),
        иначе - квадрат (False).
        """
        if self.width != self.height:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
        """
        Функция изменения размера.
        :self.width = new_width: новая ширина
        :self.height = new_height: новая высота
        """
        self.width = new_width
        self.height = new_height

    def __str__(self):
        """
        Функция вывода строки.
        :return: выводится ширина и высота
        """
        return f"ширина = {self.width}, высота = {self.height}"


rd = rectangle(30, 5)  # Назначаем ширину и высоту
print(rd)  # Выводим ширину и высоту
print('Площадь: ', rd.area())  # Выводим площадь
print('Периметр: ', rd.perimeter())  # Выводим периметр
print(rd.is_square())  # Выводим его точность
rd.resize(56, 20)  # Меняем размер
# И снова выводим площадь
print(rd)  # Выводим ширину и высоту
print('Площадь: ', rd.area())  # Выводим площадь
print('Периметр: ', rd.perimeter())  # Выводим периметр
print(rd.is_square())  # Выводим его точность
