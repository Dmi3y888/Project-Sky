text = 'apple, banana, banana, orange, orange'
dictionary = {}
res = []
for word in text.split(", "):
    # print(word)
    if dictionary.get(word) is not None:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
for key, value in dictionary.items():
    if value == max(dictionary.values()):
        res.append(key)
print(min(res))

