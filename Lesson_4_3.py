import random

lst = [1, 2, 3, 4, 5, 6, 7, 9]
#lst = [6, 3, 7]
#lst = [1, 1, 2, 1]
n = len(lst)
for i in range(n):
    lst.append(random.randint(3, 10))
    lt1, lt2, lt3 = lst[0], lst[2], lst[-1]
print([lt1, lt2, lt3])
