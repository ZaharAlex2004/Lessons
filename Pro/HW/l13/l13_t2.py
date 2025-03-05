import aiohttp
import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('http_requests.log')]
)


async def fetch_content(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    cont = await response.text()
                    return cont
                else:
                    logging.error(f"Ошибка: Страница {url} не найдена (HTTP {response.status}).")
                    return f"Ошибка: Страница {url} не найдена (HTTP {response.status})."
    except aiohttp.ClientError as e:
        logging.error(f"Ошибка при подключении к {url}: {str(e)}")
        return f"Ошибка при подключении к {url}: {str(e)}"
    except Exception as e:
        logging.exception(f"Неизвестная ошибка при обработке {url}: {str(e)}")
        return f"Неизвестная ошибка при обработке {url}: {str(e)}"


async def fetch_all(urls: list) -> tuple:
    tasks = [fetch_content(u) for u in urls]
    res = await asyncio.gather(*tasks)
    return res


if __name__ == "__main__":
    urls = ["http://gortransport.kharkov.ua/", "https://wokwi.com/", "https://example.net"]
    try:
        results = asyncio.run(fetch_all(urls))
        for url, result in zip(urls, results):
            logging.info(f"Результат для {url}: {result[:200]}...")
    except Exception as e:
        logging.error(f"Не удалось выполнить загрузку данных: {str(e)}")
