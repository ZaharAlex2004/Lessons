def second_index(text, some_str):
    ftx = text.find(some_str) != -1
    fnd = text.find(some_str) + 1
    if ftx:
        if text.find(some_str, fnd) != -1:
            stx = text.find(some_str, fnd)
        else:
            return None
    else:
        return None
    return stx


sec_i1 = second_index("sims", "s")
sec_i2 = second_index("find the river", "e")
sec_i3 = second_index("hi", "h")
sec_i4 = second_index("Hello, hello", "lo")
print(sec_i1)
print(sec_i2)
print(sec_i3)
print(sec_i4)

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
