class Built:
    """
    Класс Built.
    """
    def __init__(self, data) -> None:
        """
        Инициализация класса.
        :param data:
        """
        self.data = data

    def __len__(self) -> int:
        """
        Возвращение количества элементов в списке.
        :return:
        """
        return len(self.data)

    def __iter__(self) -> "Built":
        """
        Возвращение итератора для перебора элементов.
        :return:
        """
        self.index = 0
        return self

    def __next__(self) -> "Built":
        """
        Возвращение следующего элемента при итерировании.
        :return:
        """
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index: int) -> "Built":
        """
        Получение итератора для перебора элементов.
        :param index:
        :return:
        """
        return self.data[index]


def built_len(obj) -> int:
    """
    Возвращение следующего элемента при итерировании.
    :param obj:
    :return:
    """
    return obj.__len__()


def built_sum(obj) -> int:
    """
    Вычисления суммы элементов объекта, использующего __iter__.
    :param obj:
    :return:
    """
    total = 0
    for item in obj:
        total += item
    return total


def built_min(obj) -> int:
    """
    Нахождение минимального элемента в объекте, использующем __iter__.
    :param obj:
    :return:
    """
    iterator = iter(obj)
    min_val = next(iterator)
    for item in iterator:
        if item < min_val:
            min_val = item
    return min_val


b_lst = Built([5, 7, 9, 11, 13, 15])

print(built_len(b_lst))
print(built_sum(b_lst))
print(built_min(b_lst))
