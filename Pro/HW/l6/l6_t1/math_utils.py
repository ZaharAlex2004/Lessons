import math


def fact():
    """
    Вычисление факториала.
    :return:
    """
    print('Факториал')
    try:
        n = int(input('Enter number: '))
        print(math.factorial(n))
    except ValueError as e:
        print(e)
        return


def nod():
    """
    Вычисление НОД.
    :return:
    """
    try:
        print('НОД.')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        while b:
            a, b = b, a % b
        print(a)
    except ValueError as e:
        print(e)
        return
