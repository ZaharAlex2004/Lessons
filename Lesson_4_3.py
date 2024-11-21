import random

lst = [4, 9, 3, 5, 7, 6]

print("ДО: ", lst)

lst1 = random.sample(lst * 2, 3)

#for i in range(len(lst)):
#    random.shuffle(lst)

print("ПОСЛЕ: ", lst1)
