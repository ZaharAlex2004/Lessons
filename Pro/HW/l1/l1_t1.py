import math as mt

"""
Импорт модуля math как mt
"""


# Вычисление площади круга
def calculate_circle_area(radius: float) -> float:
    """
    Здесь мы вычисляем площадь круга.
    radius - радиус круга
    число пи = 3.14
    Число пи умножаем на указанный радиус (После ввода), умноженый в 2 раза
    """
    return mt.pi * radius ** 2


rad = float(input("Введите радиус: "))  # Вводим радиус круга
res = calculate_circle_area(rad)  # Вычисляем
print(res)  # Выводим площадь круга
