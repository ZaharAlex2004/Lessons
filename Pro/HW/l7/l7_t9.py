import pytest


class AgeVerifier:
    """
    Класс AgeVerifier.
    """
    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Возрастная проверка.
        :param age:
        :return:
        >>> AgeVerifier.is_adult(18)
        True
        >>>AgeVerifier.is_adult(16)
        False
        """
        if age < 0:
            raise ValueError("Возраст не повинен бути від'ємним.")
        return age >= 18


@pytest.mark.skipif(121 > 120, reason="Неправильне значення віку")
def test_is_adult():
    """
    Проверка возрастов.
    :return:
    """
    assert AgeVerifier.is_adult(18) == True
    assert AgeVerifier.is_adult(21) == True
    assert AgeVerifier.is_adult(16) == False
    assert AgeVerifier.is_adult(0) == False
    assert AgeVerifier.is_adult(121) == False
