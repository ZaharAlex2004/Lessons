import inspect


def analyze_inheritance(cls: type):
    """
    Анализ наследования.
    :param cls:
    :return:
    """
    # Получаем все классы в MRO (метод разрешения порядка)
    baza_mt = cls.__bases__

    # Словарь для хранения унаследованных методов
    inherited_methods = {}

    # Идем по всем классам в MRO, начиная с самого верхнего
    for base in baza_mt:
        # Получение всеч методов этого класса
        methods = inspect.getmembers(base, predicate=inspect.isfunction)
        for method_name, _ in methods:
            # Добавляем метод в результат, если он еще не добавлен
            if method_name not in inherited_methods:
                inherited_methods[method_name] = base.__name__

    # Печатаем результаты
    if inherited_methods:
        print(f"Класс {cls.__name__} следует:")
        for method, base in inherited_methods.items():
            print(f"- {method} из {base}")
    else:
        print(f"Класс {cls.__name__} не наследует методов.")


class Parent:
    """
    Родительский класс.
    """
    def parent_method(self):
        """
        Родительский метод.
        :return:
        """
        pass


class Child(Parent):
    """
    Наследственный класс.
    """
    def child_method(self):
        """
        Наследный метод.
        :return:
        """
        pass


analyze_inheritance(Child)
