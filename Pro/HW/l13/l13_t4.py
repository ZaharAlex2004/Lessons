import asyncio


async def slow_task():
    """
    Импорт выполнение задания
    :return:
    """
    print(f"Початок, очікуйте 10 секунд")
    await asyncio.sleep(10)
    print(f"Завершено")


async def main():
    """
    Основная функция для выполнения задачи
    :return:
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Перевищено час очікування, завдання не було завершено вчасно.")


if __name__ == "__main__":
    asyncio.run(main())
