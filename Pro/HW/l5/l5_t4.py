class InsufficientResourcesException(Exception):
    """
    Класс InsufficientResourcesException.
    """
    def __init__(self, required_resource: str, required_amount: float, current_amount: float) -> None:
        """
        Инициализация класса.
        :param required_resource:
        :param required_amount:
        :param current_amount:
        """
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        super().__init__(f'Insufficient funds: {required_resource}. Required: {required_amount}. You have: {current_amount}')


class Player:
    """
    Класс Player.
    """
    def __init__(self, gold: float) -> None:
        self.gold = gold

    def source(self, type_obj: str, r_gold=0) -> None:
        try:
            if self.gold < r_gold:
                raise InsufficientResourcesException(type_obj, r_gold, self.gold)

            self.gold -= r_gold
            print("Thank you! Product buyed!")

        except InsufficientResourcesException as i:
            print(i)


pl = Player(50)

pl.source("Artefact", 80)
