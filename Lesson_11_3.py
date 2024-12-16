def is_even(number):
    if not number & 1:
        return True
    else:
        return False


print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")
