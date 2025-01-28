import json


class CoffMang:
    """
    Класс CoffMang.
    """
    def __init__(self, flph):
        """
        Инициализация.
        :param flph:
        """
        self.flph = flph
        self.config = None

    def __enter__(self):
        """
        Загрузка конфигурации.
        :return:
        """
        try:
            with open(self.flph, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {}
        return self.config

    def __exit__(self, exc_t: str, exc_val: str, traceback: str) -> None:
        """
        Выход.
        :param exc_t:
        :param exc_val:
        :param traceback:
        :return:
        """
        with open(self.flph, 'w') as file:
            json.dump(self.config, file, indent=4)


config_file = 'config.json'


with CoffMang(config_file) as config:
    config['new_key'] = 'new_value'
    config['existing_key'] = 'updated_value'
