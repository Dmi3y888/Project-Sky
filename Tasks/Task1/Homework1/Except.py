f = open('numbers.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('Это не число.')
except Exception:
    print('Что это')
else:
    print('Все хорошо.')
finally:
    f.close()
    print('Close')