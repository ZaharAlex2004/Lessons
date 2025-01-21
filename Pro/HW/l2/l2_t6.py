class MyClass:
    """
    Класс MyClass.
    """
    def greet(self, name: str):
        """
        Функция приветствия.
        :param name:
        :return:
        """
        return f"Hello, {name}!"


class Proxy:
    """
    Класс Proxy.
    """
    def __init__(self, obj):
        """
        Инициализация класса.
        :param obj:
        """
        self._obj = obj

    def __getattr__(self, name: str):
        """
        Функция приёма атрибута.
        :param name:
        :return:
        """
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapped(*args: str, **kwargs: dict):
                """
                Функция проверки, является ли атрибут методом.
                :param args:
                :param kwargs:
                :return:ц
                """
                print(f"Calling method:\n{name} with args: {args}")
                return attr(*args, **kwargs)
            return wrapped
        else:
            return attr


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
