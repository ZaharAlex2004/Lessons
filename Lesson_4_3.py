import random

lst = [random.randint(3, 10) for i in range(random.randint(3, 10))]
print(lst)

for i in range(random.randint(3, 10)):
    lt1, lt2, lt3 = lst[0], lst[2], lst[-2]
print([lt1, lt2, lt3])