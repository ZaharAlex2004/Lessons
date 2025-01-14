def first_word(text):
    def dellsym(text):
        fwrd = text.replace('.', '')
        fwrd2 = fwrd.replace(',', '')
        return fwrd2

    txt = text.split()
    for fw in txt:
        if not dellsym(fw) == '':
            if "." in fw:
                fw = fw.split(".")[0]
            if "," in fw:
                fw = fw.split(",")[0]
            return dellsym(fw)


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
