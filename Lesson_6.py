from string import ascii_letters

a = ascii_letters
b = input()
c = list(b)

print(a[a.find(c[0]):a.find(c[2])+1])
