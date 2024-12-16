def generate_cube_numbers(end):
    sz = 2
    while True:
        qubik = sz ** 3
        if qubik > end:
            break
        yield qubik
        sz += 1
    return

from inspect import isgenerator

gen = generate_cube_numbers(1)
print(isgenerator(gen))
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
