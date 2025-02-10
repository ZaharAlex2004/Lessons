from typing import Union


def parse_input(n: Union[int | str]) -> int | None:
    """
    Парсинг вывода.
    :param n:
    :return:
    """
    if isinstance(n, int):
        return n
    try:
        return int(n)
    except ValueError:
        return None


print(parse_input(42))       # 42
print(parse_input("100"))    # 100
print(parse_input("hello"))  # None

