ints = []
with open('numbers.txt') as f:
    for line in f:
        ints.append(int(line))
    print('Close')

