# Вычисление площади круга

# Инициализируем функцию вычисления площади круга
# radius - радиус круга
def calculate_circle_area(radius):
    return 3.14 * radius ** 2 # Здесь мы вычисляем площадь круга


rad = float(input("Введите радиус: "))  # Вводим радиус круга
res = calculate_circle_area(rad)  # Вычисляем
print(res)  # Выводим площадь круга
