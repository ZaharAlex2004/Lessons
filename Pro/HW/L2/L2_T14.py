class TypeCheckedMeta(type):
    """
    Метакласс TypeCheckedMeta.
    """
    def __new__(cls, name: str, bases: tuple, dct: dict):
        """
        Функция создания.
        :param name:
        :param bases:
        :param dct:
        """
        annotations = dct.get('__annotations__', {})
        original_setattr = dct.get('__setattr__', object.__setattr__)

        def __setattr__(self, name: str, value: str):
            """
            Функция установки атрибута.
            :param self:
            :param name:
            :param value:
            :return:
            """
            try:
                if name in annotations:
                    expected_type = annotations[name]

                    # Проверяем, что тип значения соответствует ожидаемому
                    if not isinstance(value, expected_type):
                        raise TypeError(f"TypeError: Для атрибута '{name}' ожидается тип {expected_type}, но получен {type(value)}")
            except TypeError as e:
                print(e)

            # Устанавливаем атрибут
            return original_setattr(self, name, value)

        # Добавляем новый метод __setattr__ в класс
        dct['__setattr__'] = __setattr__

        # Создаем и возвращаем класс
        return super().__new__(cls, name, bases, dct)


class Person(metaclass=TypeCheckedMeta):
    """
    Клас Person.
    """
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int

