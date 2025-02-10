from typing import TypedDict, Optional, Protocol


class User(TypedDict):
    """
    Класс User
    """
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    """
    Класс UserDatabase.
    """
    def save_user(self, user: User) -> None:
        """
        Место сохранения пользователя.
        :param user:
        :param user:
        :return:
        """
        ...

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Место приема пользователя по ID.
        :param user_id:
        :return:
        """
        ...


class InMemoryUserDB:
    """
    Класс InMemoryUserDB.
    """
    def __init__(self):
        """
        Инициализация класса.
        """
        self.users = {}

    def save_user(self, user: User) -> None:
        """
        Сохранение пользователя.
        :param user:
        :return:
        """
        self.users[user['id']] = user

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Приём пользователя по ID.
        :param user_id:
        :return:
        """
        return self.users.get(user_id)


db = InMemoryUserDB()
db.save_user({"id": 1, "name": "Alice", "is_admin": False})
print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
print(db.get_user(2))  # None

