mas1 = [1, 1, 1, 1, 2, 7, 3, 4, 0, 1, 1, 0, 7, 9]
res = []
index = 0
while index < len(mas1) - 1:
    mas2 = []
    while index < len(mas1) - 1 and mas1[index] == mas1[index + 1]:
        mas2.append(mas1[index])
        index += 1
    mas2.append(mas1[index])
    print('mas2', mas2)
    print('res', res)
    print()
    if len(mas2) > len(res):
        res = mas2


    # print(mas1[i], mas1[i + 1])
    index += 1
print()
print()
print(res)