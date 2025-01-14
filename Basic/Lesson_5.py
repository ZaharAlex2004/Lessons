import keyword
import string

kwl = keyword.kwlist

txt = input("Введите название: ")

nums = string.digits

for i in txt:
    if i != i.upper() and txt.isidentifier() and txt not in kwl or i in nums or i in '_' and not (txt.count('__') or txt.count('___')):
        pass
    else:
        print(False)
        break
else:
    print(True)
