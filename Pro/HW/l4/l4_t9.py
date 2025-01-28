import os
import shutil


class AutoResCop:
    """
    Класс AutoResCop.
    """
    def __init__(self, cop: str) -> None:
        """
        Инициализация.
        :param cop:
        """
        self.cop = cop
        self.backup = f'{self.cop}.bak'

    def __enter__(self):
        """
        Загрузка конфигурации.
        :return:
        """
        if os.path.exists(self.cop):
            shutil.copy2(self.cop, self.backup)
        return self.cop

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        """
        Выход.
        :param exc_type:
        :param exc_value:
        :param traceback:
        :return:
        """
        if exc_type is None:
            pass
        else:
            if os.path.exists(self.backup):
                shutil.copy2(self.backup, self.backup)
        if os.path.exists(self.backup):
            os.remove(self.backup)


vasf = 'filtered_logfile.txt'

try:
    with AutoResCop(vasf) as file:
        with open(file, 'w') as f:
            f.write('New content here!')
except Exception as e:
    print(f"An error occurred: {e}")
