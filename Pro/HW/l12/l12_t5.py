import threading
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('mr_research.log')
    ]
)
logger = logging.getLogger()


def search_in_file(file_path, search_text):
    """
    Функция для поиска текста в файле
    :param file_path:
    :param search_text:
    :return:
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_text in content:
                logger.info(f"Найден текст в файле: {file_path}")
                return f"Найден текст в файле: {file_path}"
            else:
                logger.info(f"Текст не был найден в файле: {file_path}")
                return f"Текст не был найден в файле: {file_path}"
    except Exception as e:
        logger.error(f"Ошибка при обработке файла {file_path}: {e}")
        return f"Ошибка при обработке файла {file_path}: {e}"


def search_text_in_files(paths, search_text, max_workers=4):
    """
    Поиск текста в нескольких файлах с использованием потоков.
    :param paths:
    :param search_text:
    :param max_workers:
    :return:
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(search_in_file, file_path, search_text): file_path for file_path in paths}

        for future in as_completed(futures):
            result = future.result()
            print(result)


if __name__ == '__main__':
    files = [
        'mr_research.txt',
    ]

    search_text = 'Cassandra'

    search_text_in_files(files, search_text, max_workers=4)
