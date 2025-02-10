import asyncio
from typing import Awaitable, Dict, Any


class AsyncFetcher:
    """
    Класс AsyncFetcher.
    """
    async def fetch(self, url: str) -> Awaitable[Dict[str, Any]]:
        """
        Заглушка.
        :param url:
        :return:
        """
        await asyncio.sleep(1)
        return {"url": url, "status": "success", "data": {"key": "value"}}


async def main():
    """
    Заглушка.
    :return:
    """
    fetcher = AsyncFetcher()
    result = await fetcher.fetch("https://example.com/api")
    print(result)

asyncio.run(main())

