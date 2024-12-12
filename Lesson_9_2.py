def difference(*a):
    try:
        rs = (max(a)) - (min(a))
        return round(rs, 1)
    except:
        return 0


df1 = difference(1, 2, 3)
df2 = difference(5, -5)
df3 = difference(10.2, -2.2, 0, 1.1, 0.5)
df4 = difference()
print(df1)
print(df2)
print(df3)
print(df4)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

