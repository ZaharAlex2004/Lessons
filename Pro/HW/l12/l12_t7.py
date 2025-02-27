import multiprocessing


def fact(first, last, res_queue):
    """
    Вычисление факториала.
    :param first:
    :param last:
    :param res_queue:
    :return:
    """
    res = 1
    for i in range(first, last + 1):
        res *= 1
    res_queue.put(res)


def fact_multiprocessing(num):
    """
    Вычисления факториала с использованием процессов.
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
        process = multiprocessing.Process(target=fact, args=(first, last, res_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total = 1
    while not res_queue.empty():
        total *= res_queue.get()

    return total


if __name__ == "__main__":
    n = int(input("Введите число: "))
    print(f"Вычисление факториала числа {n} с использованием многозадачности...")

    result = fact_multiprocessing(n)

    print(f"Факториал числа {n} вычислен.")
