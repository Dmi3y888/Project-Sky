text1 = input("Enter text1 = ")

i = 0

text1 = text1.split(" ")

for i in text1:
    if i != " ":
        text1[i] = word2
    i=i+1
print(" ".join(text1))