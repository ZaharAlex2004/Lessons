from typing import List, Any, Dict, Optional
import pytz
import requests.exceptions
from bs4 import BeautifulSoup
import pandas as pd
import requests as r
from datetime import datetime
from dateutil import parser
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('news.log')]
)


def get_site(url: str, session: Optional[r.Session] = None) -> BeautifulSoup | None:
    """
    Функция для загрузки HTML-кода страницы
    :param url: Адрес страницы
    :param session: Объект сессии requests, если используется
    :return: объект BeautifulSoup
    """
    session = session or r.Session()
    try:
        response = session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при запросе страницы: {e}")
        return None


def news_parser(soup: "BeautifulSoup", title_tag: str = 'h1', link_tag: str = 'a', date_tag: str = 'time', summary_tag: str = 'p') -> list[dict[str, str | None | Any]]:
    """
    Функция для парсинга новостей с параметризацией тегов
    :param soup: объект BeautifulSoup
    :param title_tag: Тег для заголовка
    :param link_tag: Тег для ссылки
    :param date_tag: Тег для даты
    :param summary_tag: Тег для описания
    :return: список словарей с новостями
    """
    if not soup:
        return []

    news_lst = []
    articles = soup.find_all('article')

    if not articles:
        logging.info("Статьи не найдены на странице!")

    for a in articles:
        title_tg = a.find(title_tag)
        link_tg = a.find(link_tag)
        date_tg = a.find(date_tag)
        summary_tg = a.find(summary_tag)

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

    logging.info(f"Найдено {len(news_lst)} новостей.")
    return news_lst


def save_to_csv(data: list, filename='news.csv') -> None:
    """
    Сохранение в формат csv
    :param data: Данные сайта
    :param filename: Имя файла после сохранения
    :return:
    """
    if not data:
        logging.info("Нет данных для сохранения в CSV!")
    else:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logging.info(f"Данные сохранены в {filename}")


def data_filter(datanews: list, days=7) -> list[Any]:
    """
    Фильтрация новостей по дате
    :param datanews: Список новостей
    :param days: Количество дней для фильтрации
    :return: Отфильтрованные новости
    """
    td = datetime.now(pytz.utc)
    filtered_news = []
    error_dates = []
    for n in datanews:
        try:
            nd = parser.parse(n['date'])

            if nd.tzinfo is None:
                nd = nd.replace(tzinfo=pytz.utc)

            if (td - nd).days <= days:
                filtered_news.append(n)
        except (ValueError, TypeError) as e:
            logging.error(f"Ошибка при парсинге даты для новости: {n['date']} - {e}")
            error_dates.append(n)
            continue

    if error_dates:
        with open('errors.json', 'w') as f:
            import json
            json.dump(error_dates, f, ensure_ascii=False, indent=4)

    logging.info(f"Отфильтровано {len(filtered_news)} новостей.")
    return filtered_news


if __name__ == "__main__":

    session = r.Session()

    url = "https://atn.ua/kharkiv/ponad-2600-liudej-za-tyzhden-u-kharkovi-zakhvorily-na-hryp-ta-hrvi-467563/"
    sp = get_site(url, session=session)

    if sp:
        new = news_parser(sp)

        filters = data_filter(new, days=7)

        save_to_csv(filters)
