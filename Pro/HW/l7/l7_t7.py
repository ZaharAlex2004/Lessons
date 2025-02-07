import pytest
from pathlib import Path


class FileProcessor:
    """
    Класс FileProcessor.
    """
    @staticmethod
    def write_to_file(file_path: str, data: str):
        """
        Запись в файл.
        :return:
        """
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Считывание файла
        :param file_path:
        :return:
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден.")


def test_file_write_read(tmpdir):
    """
    Проверка считыванмия.
    :param tmpdir:
    :return:
    """
    file = tmpdir.join("read_writer.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_file_write_large_data(tmpdir):
    """
    Проверка записи файла.
    :param tmpdir:
    :return:
    """
    file = tmpdir.join("largefile.txt")
    large_data = "A" * 10**6

    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)

    assert content == large_data


def test_file_read_not_found(tmpdir):
    """
    Проверка несуществующего файла.
    :param tmpdir:
    :return:
    """
    non_existent_file = tmpdir.join("read_writer.txt")
    with pytest.raises(FileNotFoundError, match=r"Файл .* не найден."):
        FileProcessor.read_from_file(non_existent_file)
