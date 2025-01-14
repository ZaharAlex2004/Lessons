a = int(input("Введите любое число больше 0 и меньше 8639999: "))

b = a // 60 // 60 // 24
c = str(a // 60 // 60 % 24)
d = str(a // 60 % 60)
f = str(a % 60)

c1 = c.zfill(2)
d1 = d.zfill(2)
f1 = f.zfill(2)

if b % 10 == 1 and b % 100 != 11:
    day = 'день'
elif 2 <= b % 10 <= 4 and (b % 100 < 10 or b % 100 >= 20):
    day = 'дня'
else:
    day = 'дней'

res = f"{b} {day}. {c1}:{d1}:{f1}"

print("Результат: ", res)
