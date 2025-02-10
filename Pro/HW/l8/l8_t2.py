from typing import List, Tuple


def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Возрвастной фильтр.
    :param people:
    :return:
    """
    return [person for person in people if person[1] >= 18]


people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))
# [("Андрій", 25), ("Марія", 19)]
