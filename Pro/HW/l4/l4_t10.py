import zipfile
import os


class Zipper:
    """
    Класс Zipper.
    """
    def __init__(self, zip_name: str) -> None:
        """
        Инициализация класса.
        :param zip_name:
        """
        self.zip_name = zip_name

    def __enter__(self):
        """
        Запуск архивации файлов.
        :return:
        """
        self.arch = zipfile.ZipFile(self.zip_name, mode="w")
        return self.arch

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        """
        Выход.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        if self.arch:
            self.arch.close()


arch_name = 'sample.zip'

add_arch = ['hill.csv', 'l4t10.txt']

with Zipper(arch_name) as archiver:
    for file_name in add_arch:
        if os.path.exists(file_name):
            archiver.write(file_name, os.path.basename(file_name))

