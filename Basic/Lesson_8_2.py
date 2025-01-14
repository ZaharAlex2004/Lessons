def is_palindrome(text):
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum())
    if text == text[::-1]:
        return True
    else:
        return False


ipl1 = is_palindrome('A man, a plan, a canal: Panama')
ipl2 = is_palindrome('0P')
ipl3 = is_palindrome('a.')
ipl4 = is_palindrome('aurora')
print(ipl1)
print(ipl2)
print(ipl3)
print(ipl4)

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
