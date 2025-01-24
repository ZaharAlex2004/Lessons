class Person:
    """
    Класс Person
    """
    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация класса.
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def __lt__(self, other) -> bool:
        """
        Определение "старшего".
        :param other:
        :return:
        """
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __eq__(self, other) -> bool:
        """
        Определение "ровного".
        :param other:
        :return:
        """
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented

    def __gt__(self, other) -> bool:
        """
        Определение "младшего".
        :param other:
        :return:
        """
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __repr__(self) -> str:
        """
        Коректировка результатов.
        :return:
        """
        return f'{self.name}, {self.age} yerars'


socium = [
    Person('Daniel', 24),
    Person('Fedor', 27),
    Person('Victor', 26),
    Person('Joseph', 21)
]


print(sorted(socium, reverse=True))
