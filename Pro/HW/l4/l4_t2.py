import uuid


class Hasher:
    """
    Класс Hasher.
    """
    def __init__(self):
        """Инициализация класса."""
        pass

    def __iter__(self):
        """
        Итерация.
        :return:
        """
        return self

    def __next__(self):
        """
        Генерация нового уникального идентификатора (UUID)
        :return:
        """
        return str(uuid.uuid4())


itr = Hasher()

for _ in range(5):
    print(next(itr))