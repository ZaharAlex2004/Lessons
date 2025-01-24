class Fraction:
    """
    Класс Fraction
    """
    def __init__(self, num: int | float, denum: int | float) -> None:
        """
        Инициализация класса.
        :param num: числитель
        :param denum: знаменатель
        """
        self.num = num
        self.denum = denum

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Сложение дробей.
        :param other:
        :return:
        """
        return Fraction(self.num * other.denum + other.num * self.denum, self.denum * other.denum)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Вычитание дробей.
        :param other:
        :return:
        """
        return Fraction(self.num * other.denum - other.num * self.denum, self.denum * other.denum)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Умножение дробей.
        :param other:
        :return:
        """
        return Fraction(self.num * other.num, self.denum * other.denum)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Деление дробей.
        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            return Fraction(self.num / other.denum, other.num / self.num)
        return NotImplemented

    def __repr__(self) -> str:
        """
        Функция коректировки дробей.
        :return:
        """
        return f"Дробь: {self.num}, {self.denum}"


dr1 = Fraction(1, 5)
dr2 = Fraction(4, 8)
drr = dr1 + dr2
drr1 = dr1 - dr2
drr2 = dr1 * dr2
drr3 = dr1 / dr2
print(drr)
print(drr1)
print(drr2)
print(drr3)
