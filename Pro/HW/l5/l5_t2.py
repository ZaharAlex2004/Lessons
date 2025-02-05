def arithmetic_mean(fr_file: str, ex_file: str) -> None:
    """
    Вычисление среднего арифметического.
    :param fr_file:
    :param ex_file:
    :return:
    """
    try:
        find = open(fr_file, 'r')
        s = 0
        n = 0

        for line in find:
            s += int(line)
            n += 1
        find.close()
        fout = open(ex_file, 'w')

        if n != 0:
            fout.write(str(f'Result: {s / n}'))
        fout.close()
    except FileNotFoundError as f:
        print(f)
        return
    except ValueError as v:
        print(v)
        return


arithmetic_mean('srarif.txt', 'result.txt')
