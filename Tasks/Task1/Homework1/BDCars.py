DataBaseCars = {}
commands = ['Read', 'Enter', 'Search', 'Enter number', 'Enter brand', 'Enter mark', 'Enter year', 'Enter money', 'Enter km', 'Enter name', 'Exit']
file_name = 'DataBaseCars.txt'

while True:
    comand = input('Enter one of the Command from Read Base, Enter, Search: \n')
    if comand == 'Exit':
        print('Thx for visiting our base')
        break
    if comand == 'Read':
        file = open(file_name, 'r')
        database = file.read()
        print(database)
        file.close()
    elif comand == 'Enter':
        print('Enter info:\n')
        number = input('Enter number \n ')
        brand = input('Enter brand \n')
        mark = input('Enter mark \n')
        year = input('Enter year \n')
        money = input('Enter money \n')
        km = input('Enter km \n')
        name = input('Enter name \n')
        # any выдает ошибку, если введены другие данные
        if any([number, brand, mark, year, money, km, name]):
            print('Error, info is not correct')
        else:
            f = open(file_name, 'a')
            f.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(number, brand, mark, year, money, km, name))
            f.close()
    elif comand == 'Search':
        print('Enter searched info:\n')
        search = input('Search \n')

        file = open(file_name, 'r')
        for line in file:
            for word in line.split(' '):
                if word.find(search) >= 0:
                    print(line)
                    break


        file.close()



