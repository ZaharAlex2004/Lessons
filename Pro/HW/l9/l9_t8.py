import re


def delete_data(delt: str) -> list:
    """
    Извлечение всех URL из текста.
    :param delt:
    :return:
    """
    pattern = r'\/\/(.*?)\/'
    ur = re.findall(pattern, delt)
    return ur


print(delete_data('https://gortransport.kharkov.ua/'))
