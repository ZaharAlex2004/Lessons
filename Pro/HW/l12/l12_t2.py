import concurrent.futures
from PIL import Image
import os


def resizing(image_path, output_path, new_size=(800, 600)):
    """
    Функция для изменения размера изображения
    :param image_path:
    :param output_path:
    :param new_size:
    :return:
    """
    try:
        with Image.open(image_path) as img:
            img = img.resize(new_size)
            img.save(output_path)
            print(f"Изображение {image_path} успешно обработано и сохранено в {output_path}.")
    except Exception as e:
        print(f"Ошибка при обработке изображения {image_path}: {e}")


def image_processing(paths, out_dir):
    """
    Создание каталога для обработанных изображений
    :param paths:
    :param out_dir:
    :return:
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for image_path in paths:
            output_path = os.path.join(out_dir, os.path.basename(image_path))
            futures.append(executor.submit(resizing, image_path, output_path))

        for future in concurrent.futures.as_completed(futures):
            future.result()


image_paths = [
    'IMG_20200531_170241.jpg',
    '20160910_175652.jpg',
    '20160910_175221.jpg'
]


output_dir = './processed_images'


image_processing(image_paths, output_dir)
