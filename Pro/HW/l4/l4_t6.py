import os


class Catalog:
    """
    Класс Catalog.
    """
    def __init__(self, pg: str) -> None:
        """
        Инициализация класса.
        :param pg:
        """
        self.pg = pg
        self.files = os.listdir(pg)
        self.index = 0

    def __iter__(self):
        """
        Итерация.
        :return:
        """
        return self

    def __next__(self):
        """
        Обработка файлов.
        :return:
        """
        while self.index < len(self.files):
            file_name = self.files[self.index]
            self.index += 1
            file_path = os.path.join(self.pg, file_name)

            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                return file_name, file_size
        raise StopIteration


direct4 = 'E:\Програмирование\Python\Hillel\Lessons\Pro\HW\l4'

itf = Catalog(direct4)
for name, size in itf:
    print(f'Файл: {name}, Размер: {size} байт')
