import importlib
import inspect


def analyze_module(txt: str) -> None:
    """
    Функция анализа модуля.
    :param txt:
    :return:
    """
    try:
        # Загрузка динамического модуля
        module = importlib.import_module(txt)

        # Получение всеч членов модуля
        members = inspect.getmembers(module)

        # Списки для функций и классов
        functions = []
        classes = []

        # Разделение функций и классов
        for name, obj in members:
            if inspect.isfunction(obj) or inspect.isbuiltin(obj):
                try:
                    signature = str(inspect.signature(obj))
                    functions.append(f"{name}{signature}")
                except ValueError:
                    functions.append(f"{name}()")
            elif inspect.isclass(obj) and not name.startswith("__"):
                classes.append(name)

        print("Функции:")
        if functions:
            for function in functions:
                print(f"- {function}")
        else:
            print(f"- <нет функций в модуле {txt}>")

        print("\nКлассы:")
        if classes:
            for cls in classes:
                print(f"- {cls}")
        else:
            print(f"- <нет классов в модуле {txt}>")

    except ModuleNotFoundError:
        print(f"Модуль '{txt}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования:
txt = input("Введите имя модуля: ")
analyze_module(txt)
