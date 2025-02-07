import math


def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Обчислює факторіал.
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    """
    return math.factorial(n)


print(is_even(4))
print(factorial(1))
