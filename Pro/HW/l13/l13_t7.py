import time
import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Callable, List


URL = 'https://gortransport.kharkov.ua/'


def sync_request(_: int) -> int:
    """
    Синхронный режим
    :return:
    """
    response = requests.get(URL)
    return response.status_code


def thread_request(thread_count: int) -> List[int]:
    """
    Многопоточный режим
    :param thread_count:
    :return:
    """
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        return list(executor.map(sync_request, range(500)))


def process_request(process_count: int) -> List[int]:
    """
    Многопроцессорный режим
    :param process_count:
    :return:
    """
    with ProcessPoolExecutor(max_workers=process_count) as executor:
        return list(executor.map(sync_request, range(500)))


async def async_request():
    """
    Асинхронный режим
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return response.status


async def async_main():
    """
    Основная асинхронная функция
    :return:
    """
    tasks = [async_request() for _ in range(500)]
    return await asyncio.gather(*tasks)


def measure_time(func: Callable[..., None], *args: int) -> float:
    """
    Функция для измерения времени выполнения
    :param func: Функция
    :param args: Аргументы
    :return:
    """
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def main() -> None:
    """
    Основная функция для проведения тестов
    :return:
    """
    sync_time = measure_time(sync_request, 0)
    print(f"Синхронный режим: {sync_time:.2f} секунд")

    thread_time = measure_time(thread_request, 10)
    print(f"Многопоточный режим: {thread_time:.2f} секунд")

    process_time = measure_time(process_request, 4)
    print(f"Многопроцессорный режим: {process_time:.2f} секунд")

    async_time = measure_time(lambda: asyncio.run(async_main()))
    print(f"Асинхронный режим: {async_time:.2f} секунд")


if __name__ == '__main__':
    main()
