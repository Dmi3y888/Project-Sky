text1 = input("Enter text1 = ")

word1 = input("Enter word1 = ")

word2 = input("Enter word2 = ")

i = 0

text1 = text1.split(" ")

for word in text1:
    if word == word1:
        text1[i] = word2
    i=i+1
print(" ".join(text1))