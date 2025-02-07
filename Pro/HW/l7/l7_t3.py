import pytest


class UserManager:
    """
    Класс UserManager.
    """
    def __init__(self):
        """
        Инициализация класса.
        """
        self.user = []

    def add_user(self, name, age):
        """
        Добавить пользователя.
        :param name:
        :param age:
        :return:
        """
        self.user.append({"Name": name, "Age": age})

    def remove_user(self, name: str):
        """
        Удалить пользователя.
        :param name:
        :return:
        """
        self.user = [usr for usr in self.user if usr["Name"] != name]

    def get_all_users(self) -> list:
        """
        Получение списка пользователей.
        :return:
        """
        return self.user


@pytest.fixture
def user_manager():
    """
    Менеджер пользователей.
    :return:
    """
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    um.add_user("Peter", 27)
    return um


def test_add_user(user_manager):
    """
    Проверка добавления пользователя.
    :param user_manager:
    :return:
    """
    user_manager.add_user("Vlad", 24)
    user = user_manager.get_all_users()
    assert len(user) == 4
    assert user[-1] == {"Name": "Vlad", "Age": 24}


def test_remove_user(user_manager):
    """
    Проверка удаления имени пользователя.
    :param user_manager:
    :return:
    """
    user_manager.remove_user("Alice")
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert users[0] == {"Name": "Bob", "Age": 25}


def test_get_all_users(user_manager):
    """
    Тест всех пользователей.
    :param user_manager:
    :return:
    """
    users = user_manager.get_all_users()
    assert len(users) == 3
    assert users[0] == {"Name": "Alice", "Age": 30}
    assert users[1] == {"Name": "Bob", "Age": 25}
    assert users[2] == {"Name": "Peter", "Age": 27}


def test_check_minimum_users(user_manager):
    """
    Проверка количества пользователей.
    :param user_manager:
    :return:
    """
    if len(user_manager.get_all_users()) < 3:
        pytest.fail("There must be at least 3 users.")
