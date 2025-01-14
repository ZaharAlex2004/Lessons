def say_hi(name, age):
    fulltext = f"Hi. My name is {str(name)} and I'm {int(age)} years old"
    return fulltext


flt1 = say_hi("Alex", 32)
flt2 = say_hi("Frank", 68)
print(flt1)
print(flt2)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
