class DynamicProperties:
    """
    Класс динамического добавление свойств.
    """
    def __init__(self):
        """
        Инициализация динамического добавление свойства.
        """
        self._properties = {}

    def add_property(self, name: str, default_value=None):
        """
        Метод для добавления нового свойства.
        :param name:
        :param default_value:
        :return:
        """
        def getter(self):
            """
            Функция извлечения значения.
            :param self:
            :return:
            """
            return self._properties.get(name, default_value)

        # Используем сеттер для установки нового значения
        def setter(self, value: str):
            """
            Функция установки атрибута.
            :param self:
            :param value:
            :return:
            """
            self._properties[name] = value

        # Создаем свойство с помощью property()
        setattr(self.__class__, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
