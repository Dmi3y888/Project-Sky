text1 = input("Enter text1 = ")

text2 = input("Enter text2 = ")

text1 = text1.split(" ")

text2 = text2.split(" ")

res = []

for word in text1:
    if word not in text2:
        res.append(word)
print(res)
print(" ".join(res))
