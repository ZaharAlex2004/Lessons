class LimitedAttributesMeta(type):
    """
    Метакласс LimitedAttributesMeta.
    """
    def __new__(cls, name: str, bases: tuple, dct: dict):
        """
        Функця создания нового класса.
        :param name:
        :param bases:
        :param dct:
        """
        try:
            # Максимальное количество атрибутов
            max_attributes = 3
            # Только атрибуты
            attributes = [key for key, value in dct.items() if not key.startswith('__')]

            # Проверка атрибутов на максимальное количество
            if len(attributes) > max_attributes:
                raise TypeError(f"TypeError: Класс {name} не может иметь более {max_attributes} атрибутов.")

        except TypeError as e:
            print(e)

        # Если все в под конролем, создаем класс
        return super().__new__(cls, name, bases, dct)


class LimitedClass(metaclass=LimitedAttributesMeta):
    """
    Класс ограничения атрибутов
    """
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Ошибка


obj = LimitedClass()
