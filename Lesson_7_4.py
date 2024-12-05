import random


def common_elements():
	com = {i for i in range(0, 100) if i % 3 == 0 and i % 5 == 0}
	return com


dkt1 = {random.randint(0, 100) for dp1 in range(3)}
dkt2 = {random.randint(0, 100) for dp2 in range(5)}
print(dkt1, dkt2)

comm1 = common_elements()
print("Пересечение: ", comm1)
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
