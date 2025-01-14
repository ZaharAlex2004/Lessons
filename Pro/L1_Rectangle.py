def calculate_circle_area(radius):
    return 3.14 * radius ** 2


rad = float(input("Введите радиус: "))
res = calculate_circle_area(rad)
print(res)
