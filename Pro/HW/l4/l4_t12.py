class Biner:
    """
    Класс Biner.
    """
    def __init__(self, file, block_size=1024) -> None:
        """
        Инициализация класса.
        :param filepath:
        :param block_size:
        """
        self.file = file
        self.block_size = block_size
        self.total_bytes_read = 0

    def __enter__(self):
        """
        Открытие файла в бинарном режиме.
        :return:
        """
        self.file = open(self.file, 'rb')
        return self

    def read_block(self):
        """
        Чтение блока.
        :return:
        """
        block = self.file.read(self.block_size)
        if block:
            self.total_bytes_read += len(block)
        return block

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> str:
        """
        Завершение.
        :param exc_type:
        :param exc_value:
        :param traceback:
        :return:
        """
        if hasattr(self, 'file'):
            self.file.close()


bn = 'HiScore.dat'

with Biner(bn) as reader:
    while True:
        block = reader.read_block()
        if not block:
            break

print(f"Всего прочитано {reader.total_bytes_read} байт.")
