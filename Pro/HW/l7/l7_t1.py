import unittest


class StringProcessor:
    """
    Класс StringProcessor.
    """
    def reverse_string(self, s: str) -> str:
        """
        Реверс строки.
        :param s:
        :return:
        """
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """
        Делает букву прописной.
        :param s:
        :return:
        """
        if s:
            return s[0].upper() + s[1:]
        return s

    def count_vowels(self, s: str) -> int:
        """
        Возвращение количества гласных.
        :param s:
        :return:
        """
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)


sp = StringProcessor()
print(sp.reverse_string("Hello World"))
print(sp.capitalize_string("Hello World"))
print(sp.count_vowels("Hello World"))


class TestStringProcessor(unittest.TestCase):
    """
    Класс TestStringProcessor.
    """

    def setUp(self):
        """
        Выполнение метода перед каждым тестом.
        :return:
        """
        self.processor = StringProcessor()

    @unittest.skip("Проблема с пустыми строками.")
    def test_reverse_string_empty(self):
        """
        Тест на пустой строке
        :return:
        """
        self.assertEqual(self.processor.reverse_string(''), '')

    def test_reverse_string(self):
        """
        Тест на обычных строках
        :return:
        """
        self.assertEqual(self.processor.reverse_string('hello'), 'olleh')
        self.assertEqual(self.processor.reverse_string('12345'), '54321')

    def test_capitalize_string(self):
        """
        Тест на разных строках
        :return:
        """
        self.assertEqual(self.processor.capitalize_string('hello'), 'Hello')
        self.assertEqual(self.processor.capitalize_string('world'), 'World')
        self.assertEqual(self.processor.capitalize_string('123abc'), '123abc')  # Строки с цифрами не меняются

    def test_count_vowels(self):
        """
        Тест на строках с разными гласными
        :return:
        """
        self.assertEqual(self.processor.count_vowels('hello'), 2)
        self.assertEqual(self.processor.count_vowels('world'), 1)
        self.assertEqual(self.processor.count_vowels('12345'), 0)  # В строке с цифрами нет гласных
        self.assertEqual(self.processor.count_vowels('aeiou'), 5)  # Все гласные
        self.assertEqual(self.processor.count_vowels('bcdfg'), 0)  # Нет гласных

    def test_capitalize_string_empty(self):
        """
        Тест на пустой строке
        :return:
        """
        self.assertEqual(self.processor.capitalize_string(''), '')


if __name__ == '__main__':
    unittest.main()
