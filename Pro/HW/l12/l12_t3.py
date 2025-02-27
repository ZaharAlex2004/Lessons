import multiprocessing


def calc_sum(part, result_queue):
    """
    Вычисление суммы
    :param part:
    :param result_queue:
    :return:
    """
    part_sum = sum(part)
    result_queue.put(part_sum)


def split_array(arr, num_parts):
    """
    Разделение массива на части
    :param arr:
    :param num_parts:
    :return:
    """
    avg_len = len(arr) // num_parts
    return [arr[i * avg_len: (i + 1) * avg_len] for i in range(num_parts)]


def parallel_sum(arr, num_parts):
    """
    Разделение массива на части
    :param arr:
    :param num_parts:
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
    large_array = [i for i in range(1, 1000001)]
    num_parts = 4
    total_sum = parallel_sum(large_array, num_parts)
    print(f"Общая сумма массива: {total_sum}")
