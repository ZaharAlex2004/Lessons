def filter(file_path: str, keyword: str) -> str:
    """
    Генератор фильтрации строк.
    :param file_path:
    :param keyword:
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line  # Возвращаем строку, если она содержит ключевое слово


def save_filter(input_file: str, output_file: str, keyword: str) -> None:
    """
    Функция записи отфильтрованных строк в новый файл.
    :param input_file:
    :param output_file:
    :param keyword:
    :return:
    """
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for line in filter(input_file, keyword):
            out_file.write(line)


src = 'logfile.log'  # Путь к исходному файлу
fl = 'filtered_logfile.txt'  # Путь к новому файлу
kw = 'ERROR'  # Ключевое слово для фильтрации

save_filter(src, fl, kw)
