class Price:
    """
    Класс Price.
    """
    def __init__(self, torg: float) -> None:
        """
        Инициализация класса.
        :param torg:
        """
        self.torg = round(torg, 2)

    def __repr__(self):
        return f"Price({self.torg})"

    def __add__(self, other: "Price") -> "Price":
        """
        Сложения цен.
        :param other:
        :return:
        """
        if not isinstance(other, Price):
            raise ValueError("Можно складывать только с объектами типа Price")
        return Price(self.torg + other.torg)

    def __sub__(self, other: "Price") -> "Price":
        """
        Вычитания цен.
        :param other:
        :return:
        """
        if not isinstance(other, Price):
            raise ValueError("Можно вычитать только с объектами типа Price")
        return Price(self.torg - other.torg)

    def __eq__(self, other: "Price") -> float:
        """
        Сравнение цен.
        Возвращает True, если две цены равны.
        :param other:
        :return:
        """
        if not isinstance(other, Price):
            raise ValueError("Можно сравнивать только с объектами типа Price")
        return self.torg == other.torg

    def __lt__(self, other: "Price") -> float:
        """
        Сравнение цен.
        Возвращает True, если эта цена меньше другой.
        :param other:
        :return:
        """
        if not isinstance(other, Price):
            raise ValueError("Можно сравнивать только с объектами типа Price")
        return self.torg < other.torg

    def __gt__(self, other: "Price") -> float:
        """
        Сравнения цен.
        Возвращает True, если эта цена больше другой.
        :param other:
        :return:
        """
        if not isinstance(other, Price):
            raise ValueError("Можно сравнивать только с объектами типа Price")
        return self.torg > other.torg

    def get_torg(self):
        """
        Метод для получения цены в формате с двумя знаками после запятой.
        """
        return self.torg

    @classmethod
    def from_string(cls, price_str: str) -> 'Price':
        """
        Класс-метод для создания объекта Price из строки.
        Строка должна быть в формате "19.99 $" или "19.99".
        :param price_str:
        :return:
        """
        try:
            torg = float(price_str.split()[0])
            return cls(torg)
        except ValueError:
            raise ValueError("Невалидный формат строки для цены")


class PaymentGateway:
    """
    Класс PaymentGateway.
    """
    def __init__(self):
        """
        Инициализация класса.
        """
        self.balance = Price(0.0)  # Изначальный баланс

    def oplata(self, price: Price) -> str:
        """
        Обработка платежа.
        :param price:
        :return:
        """
        if self.balance < price:
            return "Недостаточно средств для оплаты"

        self.balance = self.balance - price
        return f"Оплата прошла успешно, оплачено {price.get_torg()}. Обновлён баланс: {self.balance.get_torg()}"

    def popolnenie(self, price: Price) -> None:
        """
        Пополнение счета.
        :param price:
        :return:
        """
        self.balance = self.balance + price
        print(f"Баланс пополнен на {price.get_torg()}. Обновлён баланс: {self.balance.get_torg()}")

    def dsk(self, discount: Price) -> str:
        """
        Применение скидки.
        :param discount:
        :return:
        """
        discounted_price = self.balance - discount
        return f"После применения скидки новый баланс: {discounted_price.get_torg()}"


wy = PaymentGateway()

wy.popolnenie(Price(100.00))  # Пополнение на 100
wy.popolnenie(Price(50.00))  # Пополнение на 50

# Платежи
print(wy.oplata(Price(120.00)))  # Платеж на 120
print(wy.oplata(Price(40.00)))  # Платеж на 40

# Применение скидки
print(wy.dsk(Price(10.00)))  # Применение скидки 10

