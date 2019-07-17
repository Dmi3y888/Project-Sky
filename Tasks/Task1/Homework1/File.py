f = open('text.txt', 'r')
firstLetter = f.read(1)
OtherText = f.read()
print(firstLetter)
print(OtherText)
f.close()

f = open('text.txt', 'a')
f.writelines(' - Fuckers')
f.close()

f = open('text.txt', 'r')
OtherText = f.read()
print(OtherText)