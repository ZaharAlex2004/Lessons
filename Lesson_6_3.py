a = int(input("Введите число: "))
i = 0
b = 1
a1 = len(str(a))

while i < a1:
    b = b * (a % 10)
    a = int(((a - a % 10) / 10))
    i += 1
    if i == a1:
        if b > 9:
            a = b
            b = 1
            i = 0
            a1 = len(str(a))

print("Итого:", b)
