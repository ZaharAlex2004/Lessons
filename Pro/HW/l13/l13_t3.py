import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('5_tasks.log')]
)


async def producer(queue: asyncio.queues.Queue) -> None:
    """
    Добавление 5 задач в очередь
    :param queue:
    :return:
    """
    for i in range(5):
        task = f"Задание {i + 1}"
        logging.info(f"Производитель добавляет: {task}")
        print(f"Производитель добавляет: {task}")
        await queue.put(task)
        await asyncio.sleep(1)


async def consumer(queue: asyncio.queues.Queue, consumer_id: int) -> None:
    """
    Извлечение задачи
    :param consumer_id:
    :param queue:
    :return:
    """
    while True:
        task = await queue.get()
        if task is None:
            break
        logging.info(f"Потребитель {consumer_id} выполняет: {task}")
        print(f"Потребитель {consumer_id} выполняет: {task}")
        await asyncio.sleep(2)
        queue.task_done()


async def main():
    """
    Основная асинхронная функция
    :return:
    """
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_tasks = [asyncio.create_task(consumer(queue, i + 1)) for i in range(3)]
    await producer_task
    await queue.join()

    for task in consumer_tasks:
        queue.put_nowait(None)
    await asyncio.gather(*consumer_tasks)


if __name__ == "__main__":
    asyncio.run(main())
