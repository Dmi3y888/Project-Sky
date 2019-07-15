bank = {}
commands = ['Deposit', 'Balance', 'Withdraw', 'Transfer', 'Income', 'Exit']
while True:

    comand = input('Enter one of the Command from Deposit, Balance, Withdraw, Transfer, Income: \n')

    if comand not in commands:
        print('Wrong command! Enter one of the Command from Deposit, Balance, Withdraw, Transfer, Income: \n')

    if comand == 'Exit':
        print('Thx for visiting our bank')
        break

    elif comand == 'Deposit':
        name = input('Enter name: \n')
        sum = float(input('Enter sum: \n'))
        if sum <= 0:
            print('Error, sum is not correct')
            continue
        if name in bank:
            bank[name] += sum
        else:
            bank[name] = sum
        print("Yohoo your balance is", bank[name])

    elif comand == 'Balance':
        name = input('Enter name: \n')
        if name in bank:
            print(bank[name])
        else:
            print('Error, you do not have money.')

    elif comand == 'Withdraw':
        name = input('Enter name: \n')
        sum = float(input('Enter sum: \n'))
        if sum <= 0:
            print('Error, sum is not correct')
        else:
            if name in bank:
                bank[name] -= sum
            else:
                bank[name] = sum * -1

    elif comand == 'Transfer':
        name = input('Enter name: \n')
        name1 = input('Enter name to transfer: \n')
        sum = float(input('Enter sum: \n'))
        if sum <= 0:
            print('Error, sum is not correct')
            continue
        if name in bank:
            bank[name] -= sum
            if name1 in bank:
                bank[name1] += sum
            else:
                bank[name1] = sum
        else:
            bank[name] = sum * -1
            if name1 in bank:
                bank[name1] += sum
            else:
                bank[name1] = sum
        print('Balance', bank[name], 'Balance', bank[name1])

    elif comand == 'Income':
        p = float(input('Enter % - \n'))
        if p <= 0:
            print('Error, % is not correct')
            continue
        for client, balance in bank.items():
            if balance > 0:
                bank[client] += balance * (p/100)




