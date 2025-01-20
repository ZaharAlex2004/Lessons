class SingletonMeta(type):
    """
    Метакласс SingletonMeta.
    """
    _instances = {}  # Словарь для хранения экземпляров классов

    def __call__(cls, *args, **kwargs):
        """
        Функция вызова.
        :param args:
        :param kwargs:
        :return:
        """
        # Проверка наличия экземпляра класса
        if cls not in cls._instances:
            # Создаем новый в случае отсуствия
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Возвращаем уже существующий экземпляр
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Класс Singleton.
    """
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True
