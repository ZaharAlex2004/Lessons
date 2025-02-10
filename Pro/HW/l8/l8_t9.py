from typing import Dict, Any, Final
from abc import ABC, abstractmethod


class Config:
    """
    Класс Config.
    """
    DATABASE_URI: Final = "sqlite:///:memory:"

    def __init__(self):
        """
        Инициализация класса.
        """
        raise NotImplementedError("This class cannot be instantiated.")


class BaseRepository(ABC):
    """
    Класс BaseRepository.
    """
    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """
        Место сохранение БД.
        :return:
        """
        pass


class SQLRepository(BaseRepository):
    """
    Класс SQLRepository.
    """
    def save(self, data: Dict[str, Any]) -> None:
        """
        Сохранение БД.
        :param data:
        :return:
        """
        print(f"Saving data to SQL db: {data}")


repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})

