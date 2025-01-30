class GameEventException(Exception):
    """
    Класс GameEventException.
    """
    def __init__(self, event_type, details=None) -> None:
        """
        Инициализация класса.
        :param event_type:
        :param details:
        """
        self.event_type = event_type
        self.details = details if details else {}


def event():
    """
    События.
    :return:
    """
    try:
        event_type = "death"
        details = {"cause": "atack controler", "location": "agraprom undeground"}
        raise GameEventException(event_type, details)
    except GameEventException as g:
        print(f"An event has occurred: {g.event_type}")
        print(f"Event details: {g.details}")

        if g.event_type == "death":
            print("You died! Respawning to last checkpoint...")
        elif g.event_type == "level up":
            print("Congratulations! You raised their level!")


event()
