class UnknownOperationError(Exception):
    """
    Класс неизвестной операции.
    """
    pass


print('Welcome to calculator!')


def calculate():
    """
    Функция вычисления.
    :return:
    """
    try:
        a = float(input('Enter first number: '))
        x = input('Enter command: ')
        b = float(input('Enter second number: '))

        if x == '+':
            print('Result: ', a + b)
        elif x == '-':
            print('Result:', a - b)
        elif x == '*':
            print('Result:', a * b)
        elif x == '/':
            print('Result:', a / b)
            if b != 0:
                print(a / b)
            else:
                raise ZeroDivisionError
        else:
            raise UnknownOperationError('Unknown operation!')
    except UnknownOperationError as e:
        print(e)
        return
    except ZeroDivisionError as e1:
        print(e1)
        return
    except ValueError as ERROR:
        print('Invalid number input')
        return
    d = input('Continue? ')
    if d == 'y':
        return
    elif d == 'n':
        print('Thank you for calculation!')
        quit()


while True:
    calculate()
