def is_even(digit):
    dg = int(digit)
    if dg % 2 == 0:
        return True
    else:
        return False


print(is_even(2))
print(is_even(5))
print(is_even(0))

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
