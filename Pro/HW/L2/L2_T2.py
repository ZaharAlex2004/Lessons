class Calculator:
    """
    Класс Calculator.
    Используются функции add(), subtract().
    """
    def add(self, a: int | float, b: int | float):
        """
        Функция сложения.
        :param a:
        :param b:
        :return:
        """
        return a + b

    def subtract(self, a: int | float, b: int | float):
        """
        Функция вычитания.
        :param a:
        :param b:
        :return:
        """
        return a - b


def call_function(obj, method_name: str, *args):
    """
    Функция вызова.
    :param obj:
    :param method_name:
    :param args:
    :return:
    """

    try:
        # Получение метода из obj с помощью getattr
        callme = getattr(obj, method_name)

        # Проверка атрибута
        # Проверка атрибута
        if callable(callme):
            # Вызов метода с переданными аргументами и возвращение результата
            return callme(*args)
        else:
            raise AttributeError(f'{method_name} не считается методом')
    except AttributeError as e:
        print(f'AttributeError: {e}')
    print(type(obj))


calc = Calculator()
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
