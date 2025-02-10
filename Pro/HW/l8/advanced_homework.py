from typing import Callable, Any, Dict, List


class EventDispatcher:
    def __init__(self):
        """
        Инициализация класса.
        """
        self.events: Dict[str, List[Callable[[Any], None]]] = {}

    def register_event(self, name: str, handler: Callable[[Any], None]) -> None:
        """
        Регистрация событий.
        :param name:
        :param handler:
        :return:
        """
        if name not in self.events:
            self.events[name] = []
        self.events[name].append(handler)

    def dispatch_event(self, name: str, data: Any) -> None:
        """
        Вызов всех событий.
        :param name:
        :param data:
        :return:
        """
        if name in self.events:
            for handler in self.events[name]:
                handler(data)
        else:
            print(f"Event {name} is not registred.")


dispatcher = EventDispatcher()


def on_message(data: str):
    print(f"Отримано повідомлення: {data}")


dispatcher.register_event("message", on_message)
dispatcher.dispatch_event("message", "Привіт!")
