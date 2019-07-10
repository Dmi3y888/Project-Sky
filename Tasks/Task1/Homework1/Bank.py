bank = {}
while True:

    comand = input('Enter Comand \n')
    if comand == 'Deposit':
        name = input('Enter name: \n')
        sum = float(input('Enter sum: \n'))
        if name in bank:
            bank[name] += sum
        else:
            bank[name] = sum
    if comand == 'exit':
        break
    if comand == 'Balance':
        name = input('Enter name: \n')
        if name in bank:
            print(bank[name])
        else:
            print(0)
    if comand == 'Withdrow':
        name = input('Enter name: \n')
        sum = float(input('Enter sum: \n'))
        if name in bank:
            bank[name] -= sum
        else:
            bank[name] = sum * -1
print('thx')
