import multiprocessing
import logging


logging.basicConfig(
    filename='parallel_sum_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def calc_sum(part: list, result_queue: multiprocessing.Queue) -> None:
    """
    Вычисление суммы для части массива
    :param part:
    :param result_queue:
    :return:
    """
    try:
        part_sum = sum(part)
        result_queue.put(part_sum)
        logging.info(f"Сумма части массива {part} вычислена: {part_sum}")
    except Exception as e:
        logging.error(f"Ошибка при вычислении суммы части {part}: {e}")


def split_array(arr: list, num_parts: int) -> list:
    """
    Разделение массива на части
    :param arr:
    :param num_parts:
    :return
    """
    print(type(num_parts))
    avg_len = len(arr) // num_parts
    return [arr[i * avg_len: (i + 1) * avg_len] for i in range(num_parts)]


def parallel_sum(arr: list, num_parts: int) -> int:
    """
    Параллельное вычисление суммы массива
    :param arr: Cписок чисел
    :param num_parts: Количество частей.
    :return:
    """
    parts = split_array(arr, num_parts)
    result_queue = multiprocessing.Queue()
    processes = []

    for part in parts:
        p = multiprocessing.Process(target=calc_sum, args=(part, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    return total_sum


if __name__ == "__main__":
    try:
        large_array = [i for i in range(1, 1000001)]
        num_parts = 4

        logging.info(f"Запуск вычисления суммы для массива длиной {len(large_array)} и {num_parts} частями.")
        total_sum = parallel_sum(large_array, num_parts)
        print(f"Общая сумма массива: {total_sum}")
        logging.info(f"Общая сумма массива: {total_sum}")
    except Exception as e:
        logging.error(f"Ошибка при вычислении общей суммы: {e}")
        print(f"Ошибка: {e}")
