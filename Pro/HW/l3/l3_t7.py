import math


class Vector:
    """
    Класс Vector
    """
    def __init__(self, *components) -> None:
        self.components = components

    def __add__(self, other):
        """
        Добавление.
        :param other:
        :return:
        """
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """
        Вычитание.
        :param other:
        :return:
        """
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """
        Умножение.
        :param other:
        :return:
        """
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __eq__(self, other):
        """
        Сравнение длинны. Если они равны, то True.
        :param other:
        :return:
        """
        return self.len() == other.len()

    def __lt__(self, other):
        """
        Сравнение длинны. Если меньше, то True.
        :param other:
        :return:
        """
        return self.len() < other.len()

    def __gt__(self, other):
        """
        Сравнение длинны. Если больше, то True.
        :param other:
        :return:
        """
        return self.len() > other.len()

    def len(self):
        """
        Вычисление длинны векторов.
        :return:
        """
        return math.sqrt(sum(x**2 for x in self.components))

    def __repr__(self):
        """
        Корекция результатов.
        :return:
        """
        return f'Вектор - {self.components}'


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
