def find_unique_value(some_list):
    slt = some_list[-1]
    if some_list.count(slt) == 1:
        return slt
    for pv in some_list:
        if slt != pv:
            return pv


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
