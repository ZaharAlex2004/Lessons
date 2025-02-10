def calculate_discount(price: float, discount: float) -> float:
    if discount >= 100:
        return 0
    disc = price - price * discount / 100
    return disc


print(calculate_discount(100, 20))   # 80.0
print(calculate_discount(50, 110))   # 0.0

from typing import List, Tuple


def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    return [person for person in people if person[1] >= 18]


people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))
# [("Андрій", 25), ("Марія", 19)]

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

from typing import List, Optional, TypeVar

T = TypeVar('T')


def get_first(val: List[T]) -> Optional[T]:
    return val[0] if val else None


print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None

from typing import Callable


def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    return operation(x)


def square(x: int) -> int:
    return x * x


def double(x: int) -> int:
    return x * 2


print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10
