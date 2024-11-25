a = int(input())

b = str(a // 60 // 60 // 24)
c = str(a // 60 // 60 % 24)
d = str(a // 60 % 60)
f = str(a % 60)

c1 = c.zfill(2)
d1 = d.zfill(2)
f1 = f.zfill(2)

day = "дней"

print(f"{b} {day}. {c1}:{d1}:{f1}")
