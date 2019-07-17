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
        bank[name] = bank.get(name, 0) + sum
        print("Youhoo, your balance is", bank[name])

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
            bank[name] = bank.get(name, 0) - sum
    elif comand == 'Transfer':
        name = input('Enter name: \n')
        name1 = input('Enter name to transfer: \n')
        sum = float(input('Enter sum: \n'))
        if sum <= 0:
            print('Error, sum is not correct')
            continue
        bank[name1] = bank.get(name1, 0) + sum
        bank[name] = bank.get(name, 0) - sum
        print('Balance', name , bank[name], 'Balance', name1, bank[name1])

    elif comand == 'Income':
        p = float(input('Enter % - \n'))
        if p <= 0:
            print('Error, % is not correct')
            continue
        for client, balance in bank.items():
            if balance > 0:
                bank[client] += balance * (p/100)




