import re


def date_formate(data: str) -> str:
    """
    Форматирование даты.
    :param data:
    :return:
    """
    pattern = r'(\d{2})/(\d{2})/(\d{4})'

    df = re.sub(pattern, r'\3-\2-\1', data)
    return df


print(date_formate('13/12/2024'))
