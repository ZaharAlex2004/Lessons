from typing import List, Optional, TypeVar

T = TypeVar('T')


def get_first(val: List[T]) -> Optional[T]:
    """
    Приём первого.
    :param val:
    :return:
    """
    return val[0] if val else None


print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None

