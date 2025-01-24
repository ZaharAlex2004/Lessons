import re


class User:
    """
    Класс User.
    """
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """
        Инициализация класса.
        :param first_name:
        :param last_name:
        :param email:
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        """
        Назначаем функцию имя.
        :return:
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Настройка имени.
        :param value:
        :return:
        """
        self.__first_name = value

    @property
    def last_name(self):
        """
        Назначаем функцию фамилии.
        :return:
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Настройка фамилии.
        :param value:
        :return:
        """
        self.__last_name = value

    @property
    def email(self):
        """
        Назначаем функцию email.
        :return:
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Настройка email.
        :param value:
        :return:
        """
        if not self.validator(value):
            raise ValueError(f"Invalid email format: {value}")
        self.__email = value

    def validator(self, email: str) -> bool:
        """
        Проверка коректности email.
        :param email:
        :return:
        """
        email_patt = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        return bool(re.match(email_patt, email))

    def __str__(self):
        """
        Адаптация к строкам.
        :return:
        """
        return f"{self.__first_name} {self.__last_name}, {self.__email}"


u1 = User("Михаил", "Петренко", "petrenko96@gmail.com")

print(u1)
print(u1.email)
u1.email = "petrenko96gmail.com"
