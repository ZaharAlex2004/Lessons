import aiohttp
import asyncio


async def fetch_content(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    cont = await response.text()
                    return cont
                else:
                    return f"Ошибка: Страница {url} не найдена (HTTP {response.status})."
    except aiohttp.ClientError as e:
        return f"Ошибка при подключении к {url}: {str(e)}"


async def fetch_all(urls: list) -> tuple:
    tasks = [fetch_content(u) for u in urls]
    res = await asyncio.gather(*tasks)
    return res


if __name__ == "__main__":
    urls = ["http://gortransport.kharkov.ua/", "https://wokwi.com/", "https://example.net"]
    results = asyncio.run(fetch_all(urls))
    for url, result in zip(urls, results):
        print(f"Результат для {url}: {result[:200]}...")
