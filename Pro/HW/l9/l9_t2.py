import re


def number_phone(ph_num: str) -> list:
    """
    Определение номера телефона.
    :param ph_num:
    :return:
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    nums = re.findall(pattern, ph_num)

    return nums


tel_num = """
    Вот несколько номеров:
    (123) 456-7890
    123-456-7890
    123.456.7890
    1234567890
"""

tn = number_phone(tel_num)

print(tn)

for t in tn:
    print(t)
