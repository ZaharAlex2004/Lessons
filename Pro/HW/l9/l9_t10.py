import re
from typing import Any


def text_test(text: str) -> list[Any]:
    """
    Поиск слова.
    :param text:
    :return:
    """
    pattern = r'\b[aA]\w*\b'
    txt = re.findall(pattern, text)
    return txt


print(text_test(input('Enter text: ')))
