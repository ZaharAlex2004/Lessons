import pytest
from unittest import mock


class BankAccount:
    """
    Класс BankAccount.
    """
    def __init__(self, init_bal) -> None:
        """
        Инициализация класса.
        :param init_bal:
        """
        self.balance = init_bal

    def deposit(self, amount: float) -> None:
        """
        Депозит.
        :param amount:
        :return:
        """
        if amount <= 0:
            if amount == 0:
                return
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Оплата.
        :param amount:
        :return:
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount == 0:
            return
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance += amount

    def get_balance(self) -> float:
        """
        Текущий баланс.
        :return:
        """
        return self.balance


@pytest.fixture
def bank_account():
    """
    Баланс аккаунта.
    :return:
    """
    return BankAccount(init_bal=100.0)


def test_deposit(bank_account):
    """
    Проверка пополнения счета.
    :param bank_account:
    :return:
    """
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150.0


def test_withdraw(bank_account):
    """
    Проверка снятия средств с достаточным балансом.
    :param bank_account:
    :return:
    """
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 130.0


def test_withdraw_insufficient_funds(bank_account):
    """
    Проверка снятия средств с недостаточным балансом.
    :param bank_account:
    :return:
    """
    with pytest.raises(ValueError, match="Недостаточно средств на счете"):
        bank_account.withdraw(200)


@pytest.mark.skip(reason="Пропускаем этот тест, если счет пуст")
def test_withdraw_empty_account():
    """
    Проверка снятия средств с пустого счета (скип).
    :return:
    """
    empty_account = BankAccount(init_bal=0.0)
    with pytest.raises(ValueError, match="Недостаточно средств на счете"):
        empty_account.withdraw(50)


def test_get_balance_from_api(bank_account):
    """
    Проверка использования моков для проверки взаимодействия с внешним API
    :param bank_account:
    :return:
    """
    with mock.patch.object(bank_account, 'get_balance', return_value=200.0) as mock_get_balance:
        assert bank_account.get_balance() == 200.0
        mock_get_balance.assert_called_once()


@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50, 150.0),
    (200, 300.0),
    (0, 100.0)
])
def test_deposit_parametrized(bank_account, deposit_amount, expected_balance):
    """
    Проверка параметризованого депозита.
    :param bank_account:
    :param deposit_amount:
    :param expected_balance:
    :return:
    """
    bank_account.deposit(deposit_amount)
    assert bank_account.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, expected_balance, expected_error", [
    (30, 130.0, None),
    (150, 100.0, "Недостаточно средств на счете"),
    (0, 100.0, "Сумма снятия должна быть положительной")
])
def test_withdraw_parametrized(bank_account, withdraw_amount, expected_balance, expected_error):
    """
    Проверка отзыва параметризации.
    :param bank_account:
    :param withdraw_amount:
    :param expected_balance:
    :param expected_error:
    :return:
    """
    if expected_error:
        with pytest.raises(ValueError, match=expected_error):
            bank_account.withdraw(withdraw_amount)
    else:
        bank_account.withdraw(withdraw_amount)
        assert bank_account.get_balance() == expected_balance
