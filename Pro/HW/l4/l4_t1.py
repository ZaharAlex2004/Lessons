class IterLog:
    """
    Класс IterLog.
    """
    def __init__(self, file_p: str) -> None:
        """
        Инициализация класса.
        :param file_p:
        """
        self.file_p = file_p
        self.file = None
        self.lines = []

    def __iter__(self):
        """
        Открытие файла, считывание и реверс чисел.
        :return:
        """
        self.file = open(self.file_p, 'r')
        self.lines = self.file.readlines()
        self.lines.reverse()
        return self

    def __next__(self):
        """
        Итерация файла.
        :return:
        """
        if self.lines:
            return self.lines.pop(0).strip()
        else:
            self.file.close()
            raise StopIteration


file_pt = 'file.txt'
itrt = IterLog(file_pt)

for ln in itrt:
    print(ln)
