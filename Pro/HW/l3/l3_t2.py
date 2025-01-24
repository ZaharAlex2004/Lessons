import math


class Vector:
    """
    Класс Vector
    """
    def __init__(self, x: float, y: float) -> None:
        """
        Инициализация класса.
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Добавление.
        :param other:
        :return:
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return ValueError

    def __sub__(self, other):
        """
        Вычитание.
        :param other:
        :return:
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return ValueError

    def __mul__(self, other):
        """
        Умножение.
        :param other:
        :return:
        """
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return ValueError

    def __eq__(self, other):
        """
        Сравнение длинны. Если они равны, то True.
        :param other:
        :return:
        """
        if isinstance(other, Vector):
            return self.len() == other.len()
        return NotImplemented

    def __lt__(self, other):
        """
        Сравнение длинны. Если меньше, то True.
        :param other:
        :return:
        """
        if isinstance(other, Vector):
            return self.len() < other.len()
        return NotImplemented

    def len(self):
        """
        Вычисление длинны векторов.
        :return:
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        """
        Корекция результатов.
        :return:
        """
        return f'Координаты - {self.x}, {self.y}'


vt1 = Vector(6, 8)
vt2 = Vector(4, 6)
print(vt1 + vt2)
print(vt1 - vt2)
print(vt1 * vt2)
print(vt1 < vt2)
print(vt1 > vt2)
print(vt2 < vt1)
print(vt2 > vt1)
print(vt1 == vt2)
print(vt1.len())
