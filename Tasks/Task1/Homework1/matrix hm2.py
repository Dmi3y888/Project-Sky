arrm1 = [
    [1, 2, 3],
    [2, 0, 2],
    [3, 2, 1]
]
arrm2 = [
    [4, 5, 6],
    [5, 0, 6],
    [0, 5, 4]
]

i = max(arrm2)
e = max(i)

index_row = 0
res = []

while index_row < len(arrm1):
    maxim = max(arrm2[index_row])
    # print(maxim)

    # print(arrm1[index_row])
    index_e = 0
    new_row = []
    while index_e < len(arrm1):
        e = arrm1[index_row][index_e]
        # print(e)
        new_row.append(e * maxim)

        index_e += 1


    # print(new_row)

    res.append(new_row)

    # print(res)

    index_row += 1
print(res)
# print(index_row * arrm2)
