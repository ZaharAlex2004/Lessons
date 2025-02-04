import json


def book_load(file):
    """
    Загрузка книг.
    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf-8') as file:
        return json.load(file)


def now_book(file):
    """
    Вывод доступных книг.
    :param file:
    :return:
    """
    books = book_load(file)
    print("Доступні книги")
    for book in books:
        if book["наявність"]:
            print(f"{book['назва']} от {book['автор']} ({book['рік']})")


def add_book(file, new):
    """
    Добавление книг.
    :param file:
    :param new:
    :return:
    """
    books = book_load(file)
    books.append(new)
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


j_file = 'books.json'

now_book(j_file)

new_book = {
    "назва": "Книга 3",
    "автор": "Автор 3",
    "рік": 2021,
    "наявність": True
}

add_book(j_file, new_book)

now_book(j_file)
