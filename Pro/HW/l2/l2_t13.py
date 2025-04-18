from typing import Callable, Any


class AutoMethodMeta(type):
    """
    Метакласс AutoMethodMeta.
    """
    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        Функция создания.
        :param name:
        :param bases:
        :param dct:
        """
        # Словарь для новых методов
        new_methods = {}

        # Перебор всех атрибутов в теле класса
        for key, value in dct.items():
            # Пропуск существующих методов
            if not key.startswith('__'):
                # Генерация геттера для атрибута
                new_methods[f'get_{key}'] = cls._create_getter(key)
                # Генерация сеттера для атрибута
                new_methods[f'set_{key}'] = cls._create_setter(key)

        # Объединение исходного словаря и нового метода
        dct.update(new_methods)

        # Создание класса с добавленными методами
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _create_getter(attribute: str) -> Callable[..., Any]:
        """
        Функция применения атрибутов.
        :param attribute:
        :return:
        """
        def getter(get: "AutoMethodMeta") -> "AutoMethodMeta":
            """
            Применяем атрибуты.
            :param get:
            :return:
            """
            return getattr(get, attribute)

        return getter

    @staticmethod
    def _create_setter(attribute: str) -> Callable[..., Any]:
        """
        Функция установки атрибутов.
        :param attribute:
        :return:
        """
        def setter(setting: "AutoMethodMeta", value: int) -> None:
            """
            Устанавливаем атрибуты.
            :param setting:
            :param value:
            :return:
            """
            setattr(setting, attribute, value)

        return setter


class Person(metaclass=AutoMethodMeta):
    """
    Класс Person.
    """
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
