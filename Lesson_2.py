ch = int(input("Please enter the integer number: ")[:4])
#[:4] - обмеження вводу до 4-х символів

a = ch // 1000
b = ch // 100 % 10
c = ch % 100 // 10
d = ch % 10

print(a)
print(b)
print(c)
print(d)