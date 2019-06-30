text1 = 'one, two, three'
text2 = 'two, three, one'

k = text1.replace(text2)

for word in text1:
    if word not in text2:
        res.append(word)
print(res)
print(" ".join(res))
