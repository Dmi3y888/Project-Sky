mas1 = [1, 2, 33, 22, 55, 33, 55, 77, 77, 88, 99, 199]
mas2 = []
mas3 = []
i = 0

for e in mas1:
    i = mas1.count(e)
    if i > 1:
        mas2.append(e)
    i = mas2.count(e)
    if i > 1:
        mas3.append(e)
j = 0
res2 = []
for i in mas3:
    if j < 2:
        res2.append(i)
    else:
        print(res2)
        j = 0
        res2 = []
        res2.append(i)
    j += 1
print(res2)