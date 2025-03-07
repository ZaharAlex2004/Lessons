import pytz
import requests.exceptions
from bs4 import BeautifulSoup
import pandas as pd
import requests as r
from datetime import datetime
from dateutil import parser


def get_site(url):
    """
    Функция для загрузки HTML-кода страницы
    :param url: Адрес страницы
    :return: объект BeautifulSoup
    """
    try:
        response = r.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы: {e}")
        return None


def news_parser(soup):
    """
    Функция для парсинга новостей
    :param soup: объект BeautifulSoup
    :return: список словарей с новостями
    """
    if not soup:
        return []

    news_lst = []
    articles = soup.find_all('article')

    if not articles:
        print("Статьи не найдены на странице!")

    for a in articles:
        title_tg = a.find('h1')
        link_tg = a.find('a')
        date_tg = a.find('time')
        summary_tg = a.find('p')

        title = title_tg.get_text() if title_tg else 'Неизвестно'

        link = link_tg['href'] if link_tg else None

        date = date_tg['datetime'] if date_tg else 'Неизвестно'
        summary = summary_tg.get_text() if summary_tg else 'Неизвестно'

        news_item = {
            'title': title,
            'link': link,
            'date': date,
            'summary': summary
        }
        news_lst.append(news_item)

    print(f"Найдено {len(news_lst)} новостей.")
    return news_lst


def save_to_csv(data, filename='news.csv'):
    """
    Сохранение в формат csv
    :param data: Данные сайта
    :param filename: Имя файла после сохранения
    :return:
    """
    if not data:
        print("Нет данных для сохранения в CSV!")
    else:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Данные сохранены в {filename}")


def data_filter(datanews, days=7):
    """
    Фильтрация новостей по дате
    :param datanews: Список новостей
    :param days: Количество дней для фильтрации
    :return: Отфильтрованные новости
    """
    td = datetime.now(pytz.utc)
    filtered_news = []
    for n in datanews:
        try:
            nd = parser.parse(n['date'])

            if nd.tzinfo is None:
                nd = nd.replace(tzinfo=pytz.utc)

            if (td - nd).days <= days:
                filtered_news.append(n)
        except (ValueError, TypeError):
            print(f"Ошибка при парсинге даты для новости: {n['date']}")
            continue

    print(f"Отфильтровано {len(filtered_news)} новостей.")
    return filtered_news


if __name__ == "__main__":

    url = "https://atn.ua/kharkiv/ponad-2600-liudej-za-tyzhden-u-kharkovi-zakhvorily-na-hryp-ta-hrvi-467563/"
    sp = get_site(url)

    if sp:
        new = news_parser(sp)

        filters = data_filter(new, days=7)

        save_to_csv(filters)
