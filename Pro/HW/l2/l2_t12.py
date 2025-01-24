class LoggingMeta(type):
    """
    Метакласс LoggingMeta.
    """
    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        Функция создания.
        :param name:
        :param bases:
        :param dct:
        """
        cls = super().__new__(cls, name, bases, dct)

        original_getattr = cls.__getattribute__

        def __getattribute__(self, get: str) -> str:
            """
            Функция извлечения значения.
            :param self:
            :param get:
            :return:
            """
            # Логируем доступ к атрибуту
            print(f"Logging: accessed '{get}'")
            return original_getattr(self, get)

        original_setattr = cls.__setattr__

        def __setattr__(self, set: str, value: str) -> None:
            """
            Функция установки атрибута.
            :param self:
            :param set:
            :param value:
            :return:
            """
            print(f"Logging: modified '{set}'")
            return original_setattr(self, set, value)

        # Применение изменения к метаклассу
        cls.__getattribute__ = __getattribute__
        cls.__setattr__ = __setattr__

        return cls


class MyClass(metaclass=LoggingMeta):
    """
    Класс MyClass.
    """
    def __init__(self, name: str) -> None:
        """
        Инициализация класса.
        :param name:
        """
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
