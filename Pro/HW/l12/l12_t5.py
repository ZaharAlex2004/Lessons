import threading


def search_in_file(file_path, search_text, result_list):
    """
    Функция для поиска текста в файле
    :param file_path:
    :param search_text:
    :param result_list:
    :return:
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_text in content:
                result_list.append(f"Найден текст в файле: {file_path}")
            else:
                result_list.append(f"Текст не был найден в файле: {file_path}")
    except Exception as e:
        result_list.append(f"Ошибка при обработке файла {file_path}: {e}")


def search_text_in_files(paths, search_text):
    """
    Поиск текста в нескольких файлах с использованием потоков
    :param paths:
    :param search_text:
    :return:
    """
    threads = []
    result_list = []

    for file_path in paths:
        thread = threading.Thread(target=search_in_file, args=(file_path, search_text, result_list))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for result in result_list:
        print(result)


if __name__ == '__main__':
    files = [
        'mr_research.txt'
    ]

    search_text = 'Cassandra'

    search_text_in_files(files, search_text)
