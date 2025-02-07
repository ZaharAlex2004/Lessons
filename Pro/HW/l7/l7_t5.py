import pytest


def divide(a: int, b: int) -> float:
    """
    Деление чисел.
    :param a:
    :param b:
    :return:
    """
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError as e:
        print(e)


print(divide(4, 2))


def test_divide():
    """
    Проверка деления чисел.
    :return:
    """
    assert divide(10, 2) == 5.0
    assert divide(16, 4) == 4.0
    assert divide(-8, 4) == -2.0
    assert divide(36, -6) == -6.0


def test_divide_zero():
    """
    Проверка деления на ноль.
    :return:
    """
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)


@pytest.mark.parametrize("a, b, res", [
    (10, 2, 5.0),
    (16, 4, 4.0),
    (-8, 4, -2.0),
    (36, -6, -6.0)
])
def test_divide_param(a, b, res):
    """
    Параметризация.
    :param a:
    :param b:
    :param res:
    :return:
    """
    assert divide(a, b) == res
