class MyClass:
    """
    Класс MyClass.
    """
    def __init__(self, value: str) -> None:
        """
        Конструктор класса MyClass.
        :param:value
        """
        self.value = value

    def say_hello(self) -> str:
        """
        Функция возвращения строки приветствия.
        :return:
        """
        return f"Hello, {self.value}"


def analyze_object(obj) -> None:
    """
    Функция анализа объектов.
    :param obj:
    :return:
    """
    print(f'Тип объекта {type(obj)}')

    attribut_mt = dir(obj)

    # Фильтрация нужного вывода
    public_attributes_methods = [attr for attr in attribut_mt if not attr.startswith('__')]

    # Перебор атрибутов и методов
    for attribute in public_attributes_methods:
        meta = getattr(obj, attribute)

        # Определение метода и атрибута
        if callable(meta):
            print(f"- {attribute}: <class 'method'>")
        else:
            print(f"- {attribute}: <class '{type(meta)}'>")


obj = MyClass("World")
analyze_object(obj)
