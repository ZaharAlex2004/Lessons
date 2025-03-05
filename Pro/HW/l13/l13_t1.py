import asyncio
import random
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('url_loading.log')]
)


async def download_page(url: str) -> None:
    """
    Загрузка страницы
    :param url: Адрес страницы
    :return:
    """
    delay = random.randint(1, 5)
    logging.info(f"Початок {url}")
    print(f"Початок {url}")
    await asyncio.sleep(delay)
    logging.info(f"Завершено {url} на {delay} сек.")
    print(f"Завершено {url} на {delay} сек.")


async def main(urls: list) -> None:
    """
    Основная асинхронная функция
    :param urls: Адреса страницы
    :return:
    """
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ["http://gortransport.kharkov.ua/", "https://wokwi.com/", "https://example.net"]
    asyncio.run(main(urls))
