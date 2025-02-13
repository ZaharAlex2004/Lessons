import re


def hash_text(hashtag: str) -> list:
    """
    Определение хештега.
    :param hashtag:
    :return:
    """
    pattern = r'#(\w+)'

    htg = re.findall(pattern, hashtag)

    return htg


tg = "#Шо43344"
print(hash_text(tg))
