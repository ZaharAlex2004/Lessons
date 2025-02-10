from typing import List, Callable, TypeVar


T = TypeVar('T')


class Processor:
    """
    Класс
    """
    def __init__(self, data: List[T]):
        """
        Инициализация класса.
        :param data:
        """
        self.data = data

    def apply(self, func: Callable[[T], T]) -> List[T]:
        """
        Приложить процесс.
        :param func:
        :return:
        """
        return [func(item) for item in self.data]


def double(x: int) -> int:
    """
    Умножение на 2.
    :param x:
    :return:
    """
    return x * 2


def to_upper(s: str) -> str:
    """
    Преобразователь в верхний регистр.
    :param s:
    :return:
    """
    return s.upper()


p1 = Processor([1, 2, 3])
print(p1.apply(lambda x: x * 2))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(str.upper))  # ["HELLO", "WORLD"]
