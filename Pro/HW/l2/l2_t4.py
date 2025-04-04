def say_hello(self) -> str:
    """
    Функция приветствия.
    :param self:
    :return:
    """
    return "Hello!"


def say_goodbye(self) -> str:
    """
    Функция прощание.
    :param self:
    :return:
    """
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}


def create_class(class_name: str, methods: dict) -> type:
    return type(class_name, (object,), methods)


MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
