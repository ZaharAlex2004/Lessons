num = [6, 0, 0, 2, 1, 0, 4, 0, 2, 2, 0, 8, 1]

print("ДО:", num)

f = 0
lst = len(num) - 1
i = 0

while i <= lst:
    if num[i] > 0:
        num[i], num[f] = num[f], num[i]
        f += 1
    elif num[i] < 0:
        num[i], num[lst] = num[lst], num[i]
        lst -= 1
        i -= 1
    i += 1



print("ПОСЛЕ:", num)
