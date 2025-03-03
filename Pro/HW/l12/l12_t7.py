import multiprocessing
import logging
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('factorial.log')
    ]
)
logger = logging.getLogger()


def fact(first, last, res_queue, process_id):
    """
    Вычисление факториала для части диапазона.
    :param first:
    :param last:
    :param res_queue:
    :param process_id:
    :return:
    """
    try:
        res = 1
        for i in range(first, last + 1):
            res *= i

        logger.info(f"Процесс {process_id} завершил вычисление факториала для диапазона {first}-{last}.")
        res_queue.put(res)
    except Exception as e:
        logger.error(f"Ошибка в процессе {process_id}: {e}")


def fact_multiprocessing(num):
    """
    Вычисление факториала с использованием процессов и многозадачности.
    :param num:
    :return:
    """
    num_processes = 4
    step = num // num_processes
    processes = []
    res_queue = multiprocessing.Queue()

    for i in range(num_processes):
        first = i * step + 1
        last = (i + 1) * step if i < num_processes - 1 else num
        process = multiprocessing.Process(target=fact, args=(first, last, res_queue, i + 1))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total = 1
    while not res_queue.empty():
        total *= res_queue.get()

    return total


if __name__ == "__main__":
    try:
        n = int(input("Введите число для вычисления факториала: "))
        logger.info(f"Вычисление факториала числа {n} с использованием многозадачности...")

        start_time = time.time()
        result = fact_multiprocessing(n)
        end_time = time.time()

        logger.info(f"Факториал числа {n} вычислен. Результат: {result}")
        logger.info(f"Время выполнения: {end_time - start_time:.2f} секунд.")

    except ValueError as e:
        logger.error(f"Ошибка ввода: {e}")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
