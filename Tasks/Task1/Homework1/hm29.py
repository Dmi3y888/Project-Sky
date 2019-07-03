mas1 = [1, 2, 7, 3, 4, 0, 1, 1, 0, 7, 9]
mas2 = [1, 3, 4, 3, 5, 0, 5, 1, 0, 0, 9]
index = 0
res = []
for e in mas1:
    if e in mas2 and e not in res:
        res.append(e)
print('X', res)
s = sum(res)
print('Sum', s)
m = max(res)
print('Max', m)