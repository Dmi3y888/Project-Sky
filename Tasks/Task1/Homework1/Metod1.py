text = input("Enter text: ")

# what is split
arr = text.split(" ")
print(arr)

for word in text.split(" "):
    if word == word[::-1]:
        print(word)