import keyword

txt = input("Введите название: ")

kwl = keyword.kwlist


if txt.isidentifier() and txt[0] != '_' and not txt.count('__') and not txt.count('___') and txt.find("_") and txt not in kwl and txt.islower():
    print(True)
else:
    print(False)
