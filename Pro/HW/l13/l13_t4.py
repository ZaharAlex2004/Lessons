import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('site_requests.log')]
)


async def slow_task():
    """
    Импорт выполнение задания
    :return:
    """
    logging.info(f"Початок, очікуйте 10 секунд")
    print(f"Початок, очікуйте 10 секунд")
    await asyncio.sleep(10)
    logging.info(f"Завершено")
    print(f"Завершено")


async def main():
    """
    Основная функция для выполнения задачи
    :return:
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        logging.info("Перевищено час очікування, завдання не було завершено вчасно.")
        print("Перевищено час очікування, завдання не було завершено вчасно.")


if __name__ == "__main__":
    asyncio.run(main())
