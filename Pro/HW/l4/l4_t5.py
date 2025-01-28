class Generator:
    """
    Класс Generator.
    """
    def __init__(self, generator: 'Generator', limit: int) -> None:
        """
        Инициализация класса.
        :param generator:
        :param limit:
        """
        self.generator = generator
        self.limit = limit

    def __enter__(self):
        """
        Создание генератора.
        :return:
        """
        self.count = 0
        return self

    def __iter__(self):
        """
        Ограничение количества элементов для генерации.
        :return:
        """
        for number in self.generator:
            if self.count >= self.limit:
                break
            self.count += 1
            yield number

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        """
        Завершение работы менеджера контекста.
        :param exc_type:
        :param exc_value:
        :param traceback:
        :return:
        """
        pass


def gener():
    """
    Генерация четнрных чисел.
    :return:
    """
    num = 0
    while True:
        yield num
        num += 2


def savig(num, fl):
    """
    Сохрананение на определенный файл.
    :param num:
    :param fl:
    :return:
    """
    with open(fl, 'w', encoding='utf-8') as file:
        for number in num:
            file.write(f"{number}\n")


generate = gener()
limit = 100

with Generator(generate, limit) as max_g:
    savig(max_g, 'gener.txt')
