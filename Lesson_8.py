def add_one(some_list):
    lst = int(''.join(map(str, some_list))) + 1
    res = [int(i) for i in str(lst)]
    return res


ao1 = add_one([1, 2, 3, 4])
ao2 = add_one([9, 9, 9])
ao3 = add_one([0])
ao4 = add_one([9])
print(ao1)
print(ao2)
print(ao3)
print(ao4)

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
