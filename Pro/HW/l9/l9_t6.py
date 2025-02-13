import re


def passwords(passer: str) -> None:
    """
    Проверка пароля.
    :param passer:
    :return:
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&!&*])[A-Za-z\d@#$%^&!&*]{8,}$'

    if re.fullmatch(pattern, passer):
        print('Welcome!')
    else:
        print('Error!')


passwords(input())
