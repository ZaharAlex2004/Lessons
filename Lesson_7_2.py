def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text += '.'
    return text


cs1 = correct_sentence("greetings, friends")
cs2 = correct_sentence("hello")
cs3 = correct_sentence("Greetings. Friends")
cs4 = correct_sentence("Greetings, friends.")
cs5 = correct_sentence("greetings, friends.")
print(cs1)
print(cs2)
print(cs3)
print(cs4)
print(cs5)

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
