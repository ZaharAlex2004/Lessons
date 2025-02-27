import threading
import requests
from urllib.parse import urlsplit
import os


def download_file(url, save_path):
    """
    Загрузкам файлов
    :param url:
    :param save_path:
    :return:
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        filename = os.path.basename(urlsplit(url).path)
        full_save_path = os.path.join(save_path, filename)

        with open(full_save_path, 'wb') as f:
            f.write(response.content)
        print(f"Файл {filename} успешно загружен.")
    except requests.RequestException as e:
        print(f"Ошибка при загрузке файла {url}: {e}")


def download_files_concurrently(urls, save_path):
    """
    Запуск файлов
    :param urls:
    :param save_path:
    :return:
    """
    threads = []

    for url in urls:
        thread = threading.Thread(target=download_file, args=(url, save_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


urls = [
    'https://gortransport.kharkov.ua/trol/ps/laz-e183/photo/kht_laz-e183_3405_20150822_v1.jpg',
    'https://cdncontribute.geeksforgeeks.org/wp-content/uploads/SQL-Manual.pdf',
]

save_path = './downloads'

if not os.path.exists(save_path):
    os.makedirs(save_path)

download_files_concurrently(urls, save_path)
