class MutableClass:
    """
    Класс методов динамического добавления и удаления атрибутов объекта.
    """
    def __init__(self):
        self.__dict__ = {}

    def add_attribute(self, name: str, value: str) -> None:
        """
        Добавление атрибутов
        :param name:
        :param value:
        :return:
        """
        setattr(self, name, value)


    def remove_attribute(self, name: str) -> None:
        """
        Удаление атрибутов.
        :param name:
        :return:
        """
        # Проверяем, есть ли атрибут
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Атрибут '{name}' не существует")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений
