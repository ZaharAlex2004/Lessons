def running_average(path: str) -> str:
    """
    Просмотр сведений.
    :param path:
    :return:
    """
    total = 0
    count = 0

    with open(path, 'r') as f:
        for line in f:
            try:
                value = float(line.strip())
                total += value
                count += 1
                yield total / count
            except ValueError:
                continue


pt = 'logfile.log'
for avg in running_average(pt):
    print(f"Текущее среднее: {avg}")
