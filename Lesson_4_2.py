lst = [4, 2, 1, 9, 0, 5]

print(lst)

i = 0

for i in range(len(lst) - 1):
    if lst:
        e = sum(lst[::2]) * lst[-1]
print(e, end=" ")
