def calculate_discount(price: float, discount: float) -> float:
    """
    Вычисление дисконта.
    :param price:
    :param discount:
    :return:
    """
    if discount >= 100:
        return 0
    disc = price - price * discount / 100
    return disc


print(calculate_discount(100, 20))   # 80.0
print(calculate_discount(50, 110))   # 0.0
