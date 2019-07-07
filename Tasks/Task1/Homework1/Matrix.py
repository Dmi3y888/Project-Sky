arr = [
    [1, 2, 3],
    [2, 0, 2],
    [3, 2, 1]
]
x = 3
index = 0
while index < len(arr):
    print(arr[index])

    index_e = 0

    while index_e < len(arr[index]):
        print(arr[index][index_e])
        index_e += 1

    index += 1
