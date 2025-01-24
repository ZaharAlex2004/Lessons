class ProductWithGetSet:
    """
    Класс ProductWithGetSet.
    """
    def __init__(self, name: str, price: float) -> None:
        """
        Инициализация класса.
        :param name:
        :param price:
        """
        self.__price = None
        self.__name = name
        self.set_price(price)

    def get_price(self):
        """
        Установка
        :return:
        """
        return f'Цена: {self.__price} грн.'

    def set_price(self, value: float):
        if value < 0:
            raise ValueError("Цена не можеть быть отрицательной.")
        self.__price = value

    def __str__(self):
        """
        Вывод строки.
        :return:
        """
        return f'{self.__name}, {self.__price} грн.'


class ProductWithProperty:
    """
    Класс ProductWithProperty.
    """
    def __init__(self, name: str, price: float) -> None:
        """
        Инициализация класса.
        :param name:
        :param price:
        """
        self.__price = price
        self.__name = name

    @property
    def price(self):
        """
        Вывод цены.
        :return:
        """
        return f'Цена: {self.__price} грн.'

    @price.setter
    def price(self, value: float) -> None:
        """
        Настройка цены.
        :param value:
        :return:
        """
        if value < 0:
            raise ValueError("Цена не можеть быть отрицательной.")
        self.__price = value

    def __str__(self):
        return f'{self.__name}, {self.__price} грн.'


class PriceDescriptor:
    """
    Класс PriceDescriptor.
    """
    def __get__(self, instance: 'ProductWithDescriptor', owner: type):
        """
        Получение цен.
        :param instance:
        :param owner:
        :return:
        """
        return f'{instance._price} грн.'

    def __set__(self, instance: 'ProductWithDescriptor', value: float):
        """
        Установка цены.
        :param instance:
        :param value:
        :return:
        """
        if value < 0:
            raise ValueError("Цена не можеть быть отрицательной.")
        instance._price = value


class ProductWithDescriptor:
    """
    Класс ProductWithDescriptor.
    """
    def __init__(self, name: str, price: float) -> None:
        """
        Инициализация класса.
        :param name:
        :param price:
        """
        self._price = price
        self.__name = name

    price = PriceDescriptor()

    def __str__(self):
        return f'{self.__name}, {self._price} грн.'


def testing():
    """
    Тестируем.
    :return:
    """
    print('\nGettter\n')
    prd = ProductWithGetSet("Картофель", 45)
    print(prd)
    print(prd.get_price())
    prd.set_price(50)
    print("Новая цена:", prd.get_price())

    print('\nProperty\n')
    prog = ProductWithProperty("Картофель", 45)
    print(prog)
    print(prog.price)
    prog.price = 52
    print("Новая цена:", prog.price)

    print('\nDescriptor\n')
    prog1 = ProductWithDescriptor("Картофель", 45)
    print(prog1)
    print("Цена:", prog1.price)
    prog1.price = 52
    print("Новая цена:", prog1.price)

testing()

'''
Больше всего я предпочитаю использовать сеттеры/геттеры. Его
достоинство - удобство в использовании. А на остальных нужно
писать больше кода.
'''
