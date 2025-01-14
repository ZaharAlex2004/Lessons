def prime_generator(end):
    prs = {}
    p = 2
    while p <= end:
        if p not in prs:
            yield p
            prs[p * p] = [p]
        else:
            for s in prs[p]:
                prs.setdefault(s + p, []).append(s)
            del prs[p]
        p += 1

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
