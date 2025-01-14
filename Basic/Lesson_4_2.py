lst = [4, 2, 1, 9, 0, 5]

print(lst)

if lst:
    e = sum(lst[::2]) * lst[-1]
else:
    e = 0

print(e, end=" ")
