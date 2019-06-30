a = [1, 2, 3, 4, 5, 6, 7]
b = [9, 8, 7, 6, 5, 4, 3]

l, s = ((a, b), (b, a))[a < b]
print([l[x] + s[x] if x < len(s) else l[x] + 0 for x in range(len(l))])
