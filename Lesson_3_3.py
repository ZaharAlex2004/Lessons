lst = [6, 5, 5, 3, 5, 8]

print(lst)
n = len(lst)

if n % 2 == 0:
    s = n // 2
else:
    s = n // 2 + 1

lt1, lt2 = lst[:s], lst[s:]
print([lt1, lt2])
