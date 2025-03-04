import concurrent.futures
from PIL import Image
import os
import logging


logging.basicConfig(
    filename='image_processing_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def resizing(image_path: str, output_path: str, new_size=(800, 600)) -> None:
    """
    Изменения размера изображения с отображением прогресса.
    :param image_path: Файл изображения
    :param output_path: Выходной путь
    :param new_size:
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(new_size)
            img.save(output_path)
            logging.info(f"Изображение {image_path} успешно обработано и сохранено в {output_path}.")
            print(f"Изображение {image_path} успешно обработано и сохранено в {output_path}.")
    except Exception as e:
        logging.error(f"Ошибка при обработке изображения {image_path}: {e}")
        print(f"Ошибка при обработке изображения {image_path}: {e}")


def image_processing(paths: list[str], out_dir: str, max_workers=5) -> None:
    """
    Обработка изображений с ограничением количества потоков.
    :param paths: Путь
    :param out_dir: Выходная директория
    :param max_workers: Максимальное число потоков
    """

    if not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir)
            logging.info(f"Каталог для сохранения файлов '{out_dir}' успешно создан.")
        except Exception as e:
            logging.error(f"Ошибка при создании каталога {out_dir}: {e}")
            print(f"Ошибка при создании каталога {out_dir}: {e}")
            return

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for image_path in paths:
            output_path = os.path.join(out_dir, os.path.basename(image_path))
            futures.append(executor.submit(resizing, image_path, output_path))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Ошибка при завершении потока обработки изображения: {e}")
                print(f"Ошибка при завершении потока обработки изображения: {e}")


image_paths = [
    'IMG_20200531_170241.jpg',
    '20160910_175652.jpg',
    '20160910_175221.jpg'
]

output_dir = './processed_images'


image_processing(image_paths, output_dir, max_workers=3)
