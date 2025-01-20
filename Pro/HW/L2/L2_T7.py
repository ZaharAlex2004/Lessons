def log_method(method):
    """
    Функция логирования меттода.
    :param method:
    :return:
    """
    # Декоратор для логирования вызова метода
    def wrapper(self, *args, **kwargs):
        print(f"Logging: {method.__name__} called with {args}")
        return method(self, *args, **kwargs)
    return wrapper


def log_methods(cls):
    """
    Функция проверки атрибутов.
    :param cls:
    :return:
    """
    for attr_name, attr_value in cls.__dict__.items():
        # Если атрибут - это метод (функция)
        if callable(attr_value):
            # Заменяем метод на обёрнутую версию с декоратором
            setattr(cls, attr_name, log_method(attr_value))
    return cls


@log_methods
class MyClass:
    """
    Вычислительный класс.
    """
    def add(self, a, b):
        """
        Функция сложения.
        :param a:
        :param b:
        :return:
        """
        return a + b

    def subtract(self, a, b):
        """
        Функция вычитания.
        :param a:
        :param b:
        :return:
        """
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)