from typing import Callable


def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    """
    Приложить операцию.
    :param x:
    :param operation:
    :return:
    """
    return operation(x)


def square(x: int) -> int:
    """
    Квадрат.
    :param x:
    :return:
    """
    return x * x


def double(x: int) -> int:
    """
    Умножение на 2.
    :param x:
    :return:
    """
    return x * 2


print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10

