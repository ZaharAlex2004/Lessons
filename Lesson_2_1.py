ch1 = int(input("Введите номер: "))

ch2 = 0

while ch1 > 0:
    d = ch1 % 10
    ch1 = ch1 // 10
    ch2 = ch2 * 10 + d

print("Обратный номер: ", ch2)