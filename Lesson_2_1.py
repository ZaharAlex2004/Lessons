c = int(input("Введите номер: "))

c5 = c % 10
c4 = c // 10 % 10
c3 = c // 100 % 10
c2 = c // 1000 % 10
c1 = c // 10000 % 10

rev = c5 * 10000 + c4 * 1000 + c3 * 100 + c2 * 10 + c1 * 1

print("Обратный номер: ", rev)