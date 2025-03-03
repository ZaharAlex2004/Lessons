import logging
import requests
import concurrent.futures
import os
from urllib.parse import urlsplit


def download_file(url, save_path):
    """
    Загрузкам файлов
    :param url:
    :param save_path:
    :return:
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filename = os.path.basename(urlsplit(url).path)
        full_save_path = os.path.join(save_path, filename)

        total_size = int(response.headers.get('Content-Length', 0))
        downloaded_size = 0

        with open(full_save_path, 'wb') as f:
            for data in response.iter_content(chunk_size=8192):
                f.write(data)
                downloaded_size += len(data)

                progress = downloaded_size / total_size * 100 if total_size > 0 else 0
                print(f"Загрузка {filename}: {progress:.2f}% ({downloaded_size}/{total_size} байт)", end='\r')
        logging.info(f"Файл {filename} успешно загружен в {full_save_path}.")
        print(f"\nФайл {filename} успешно загружен.")
    except requests.RequestException as e:
        logging.error(f"Ошибка при загрузке файла {url}: {e}")
        print(f"Ошибка при загрузке файла {url}: {e}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении файла {url}: {e}")
        print(f"Ошибка при сохранении файла {url}: {e}")


def download_files_concurrently(urls, save_path, max_workers=5):
    """
    Запуск файлов
    :param urls:
    :param save_path:
    :param max_workers:
    :return:
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

        # Использование ThreadPoolExecutor с ограничением максимального числа потоков
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(download_file, url, save_path))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Ошибка при завершении потока: {e}")
                print(f"Ошибка при завершении потока: {e}")


urls = [
    'https://gortransport.kharkov.ua/trol/ps/laz-e183/photo/kht_laz-e183_3405_20150822_v1.jpg',
    'https://cdncontribute.geeksforgeeks.org/wp-content/uploads/SQL-Manual.pdf',
    'https://www.example.com/somefile.jpg',
    'https://www.example.com/anotherfile.pdf'
]

save_path = './downloads'

if not os.path.exists(save_path):
    os.makedirs(save_path)

download_files_concurrently(urls, save_path, max_workers=3)
