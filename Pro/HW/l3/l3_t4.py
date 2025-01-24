class BinaryNumber:
    """
    Класс BinaryNumber
    """
    def __init__(self, value: str) -> None:
        """
        Инициализация класса и проверка значения.
        :param value:
        """
        if not all(bit in '01' for bit in value):
            raise ValueError("Value must be a binary string")
        self.value = value

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Функция 'AND'.
        :param other: 
        :return: 
        """
        max_len = max(len(self.value), len(other.value))
        sl_pad = self.value.zfill(max_len)
        other_pad = other.value.zfill(max_len)
        result = ''.join('1' if sl_pad[i] == '1' and other_pad[i] == '1' else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Функция 'ИЛИ'.
        :param other:
        :return:
        """
        max_len = max(len(self.value), len(other.value))
        sl_pad = self.value.zfill(max_len)
        other_pad = other.value.zfill(max_len)
        result = ''.join('1' if sl_pad[i] == '1' and other_pad[i] == '1' else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Функция 'XOR'.
        :param other:
        :return:
        """
        max_len = max(len(self.value), len(other.value))
        sl_pad = self.value.zfill(max_len)
        other_pad = other.value.zfill(max_len)
        result = ''.join('1' if sl_pad[i] != other_pad[i] else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __invert__(self) -> "BinaryNumber":
        """
        Функция 'NOT'.
        :return:
        """
        result = ''.join('1' if bit == '0' else '0' for bit in self.value)
        return BinaryNumber(result)

    def __repr__(self) -> str:
        return f'{self.value}'


if __name__ == "__main__":
    a = BinaryNumber(input('Введите первое число: '))
    b = BinaryNumber(input('Введите второе число: '))

    print(f'a & b = {a & b}')
    print(f'a | b = {a | b}')
    print(f'a ^ b = {a ^ b}')
    print(f'~a = {~a}')
    print(f'~b = {~b}')
