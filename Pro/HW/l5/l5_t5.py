class InsufficientFundsException(Exception):
    def __init__(self, required_amount: str, current_balance: float, currency="USD", transaction_type="withdrawal") -> None:
        """
        Инициализация класса.
        :param required_amount:
        :param current_balance:
        :param currency:
        :param transaction_type:
        """
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        super().__init__(f'Insufficient funds: {required_amount} {currency}. You have: {current_balance} {currency}')


class Client:
    """
    Класс Client.
    """
    def __init__(self, balance: float, curs="USD") -> None:
        """
        Инициализация класса.
        :param balance:
        :param curs:
        """
        self.balance = balance
        self.curs = curs

    def transaction_withdrawal(self, amount: float) -> None:
        """
        Снятие.
        :param amount:
        :return:
        """
        try:
            if amount > self.balance:
                raise InsufficientFundsException(required_amount=amount, current_balance=self.balance, currency=self.curs, transaction_type="withdrawal")

            self.balance -= amount
            print(f'Operation is completed. Withdraw: {amount}{self.curs}. Balance: {self.balance}{self.curs}')
        except InsufficientFundsException as e:
            print(e)

    def transaction_purchase(self, amount=0.0) -> None:
        """
        Покупка.
        :param amount:
        :return:
        """
        try:
            if amount > self.balance:
                raise InsufficientFundsException(required_amount=amount, current_balance=self.balance, currency=self.curs, transaction_type="purchase")

            self.balance -= amount
            print(f'Operation is completed. Withdraw: {amount} {self.curs}. Balance: {self.balance} {self.curs}')
        except InsufficientFundsException as e:
            print(e)


c = Client(220)
c.transaction_withdrawal(150)
c.transaction_purchase(150)
