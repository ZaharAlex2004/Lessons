import csv
from PIL import Image


def csv_save(files: str, csv_w: str) -> None:
    """
    Сохраненик csv файла.
    :param files:
    :param csv_w:
    :return:
    """
    with Image.open(files) as img:
        img.load()
        sz = img.size
        fmt = img.format
        md = img.mode
        data = [
            [f"{files}"],
            [f"Size: {sz}"],
            [f"Format: {fmt}"],
            [f"Mode: {md}"]
        ]
        with open(csv_w, 'w', encoding='utf-8') as file:
            hl = csv.writer(file)
            hl.writerows(data)


csv_save('hill.jpg', 'hill.csv')


