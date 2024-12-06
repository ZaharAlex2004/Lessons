import collections


def find_unique_value(some_list):
    for v, c in collections.Counter(some_list).items():
        if c == 1:
            return v


fuv1 = find_unique_value([1, 2, 1, 1])
fuv2 = find_unique_value([2, 3, 3, 3, 5, 5])
fuv3 = find_unique_value([5, 5, 5, 2, 2, 0.5])
print(fuv1)
print(fuv2)
print(fuv3)

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
